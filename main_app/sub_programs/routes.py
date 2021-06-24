from sub_programs.forms import Movie_Review_Form, Login_Form, Delete_Confirm
from sub_programs import models
from sub_programs import app, db
from flask import render_template, request, url_for
from sub_programs.models import Movies, MovieReviews, ReviewLikes, Users

@app.route("/")
@app.route("/home")

def home_page():
    return render_template('index.html')

@app.route("/movies")
def view_movies():
    return render_template('movies.html', items = Movies.query.order_by(Movies.movie_title))

@app.route("/movies/reviews/<movie_title>/<movie_id>", methods=['GET', 'POST'])
def movie_reviews_page(movie_title, movie_id):

    form = Movie_Review_Form()

    selected_movie = Movies.query.get(movie_id)
    try:
        selected_movie.movie_title
    except:
        return render_template("not_found.html")

    try:
        reviews = MovieReviews.query.filter_by(movie_id=int(selected_movie.id)).all()

    except:
        reviews = 0

    return render_template("review_page.html", item=selected_movie, reviews=reviews, MovieReviews=MovieReviews, form=form)

@app.route("/not_recognised")
def not_recognised():
    return render_template("not_found.html")

@app.route("/admin_page/<username>/<password>")
def admin_page(username, password):
    return "logged in"

@app.route("/login_page", methods=['GET', 'POST'])
def login_page():
    form = Login_Form()

    message = ''

    if form.validate_on_submit():

        valid_user = Users.query.filter_by(username=str(form.form_username.data)).first()

        if valid_user == None:
            message = "User not found"
            return render_template("login.html", form=form, message=message)

        if valid_user != None and valid_user.password == form.form_password.data:
            return render_template("user_home.html",items = Movies.query.order_by(Movies.movie_title), user=form.form_username.data, password=form.form_password.data)

        else:
            message = "Incorrect password"
            return render_template("login.html", form=form, message=message)
 
    else:
        return render_template("login.html", form=form, message=message)

@app.route("/delete/<movie_id>/<user>")
def delete_movie(movie_id, user):

    form = Delete_Confirm()

    UserAccount = Users.query.filter_by(username=str(user)).first()
    password = UserAccount.password

    if user == "" or password == "":
        return render_template("index.html")

    item_to_delete = Movies.query.filter_by(id=movie_id).first()

    print(item_to_delete.id)

    return render_template("delete.html", form=form, item=item_to_delete, user=user, password=password)
