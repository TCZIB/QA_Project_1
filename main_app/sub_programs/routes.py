from sub_programs.forms import Movie_Review_Form, Login_Form, Modify_Confirm
from sub_programs import models
from sub_programs import app, db
from flask import render_template, request, url_for, redirect
from sub_programs.models import Movies, MovieReviews, ReviewLikes, Users
from sub_programs import profanities

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

    if form.validate_on_submit():

        review_content = form.review.data
        review_author = form.username.data

        review_content_test = review_content.split()

        for word in review_content_test:
            for bad_word in profanities:
                if word == bad_word:
                    message = f"{word} Not allowed!"
                    return render_template("review_page.html", item=selected_movie, reviews=reviews, MovieReviews=MovieReviews, form=form, message=message)

        new_review = MovieReviews(movie_id=selected_movie.id, review_contents=review_content, review_author=review_author)

        db.session.add(new_review)
        db.session.commit()

        return render_template("review_page.html", item=selected_movie, reviews=reviews, MovieReviews=MovieReviews, form=form)

    return render_template("review_page.html", item=selected_movie, reviews=reviews, MovieReviews=MovieReviews, form=form)

@app.route("/not_recognised")
def not_recognised():
    return render_template("not_found.html")

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
            return redirect(url_for("logged_in", user=form.form_username.data, password=form.form_password.data))

        else:
            message = "Incorrect password"
            return render_template("login.html", form=form, message=message)
 
    else:
        return render_template("login.html", form=form, message=message)

@app.route("/logged_in/<user>/<password>", methods=['GET', 'POST'])
def logged_in(user, password):

    form = Modify_Confirm()

    if form.validate_on_submit():
    
            form_movie_title = form.movie_title.data
            form_movie_age = form.movie_age.data
            form_movie_description = form.movie_description.data
            form_movie_runtime = form.movie_runtime.data
            form_movie_cover_art = form.movie_cover_art.data

            if not form_movie_cover_art:
                message = "Empty movie cover art"
                return render_template("user_home.html",items = Movies.query.order_by(Movies.movie_title), user=user, password=password, message_add_error=message, form=form)

            if not form_movie_title:
                message = "Empty movie title"
                return render_template("user_home.html",items = Movies.query.order_by(Movies.movie_title), user=user, password=password, message_add_error=message, form=form)

            if not form_movie_age:
                message = "Empty movie age - rating"
                return render_template("user_home.html",items = Movies.query.order_by(Movies.movie_title), user=user, password=password, message_add_error=message, form=form)

            if not form_movie_description:
                message = "Empty movie description"
                return render_template("user_home.html",items = Movies.query.order_by(Movies.movie_title), user=user, password=password, message_add_error=message, form=form)

            if not form_movie_runtime:
                message = "Empty movie runtime"
                return render_template("user_home.html",items = Movies.query.order_by(Movies.movie_title), user=user, password=password, message=message, form=form)
            
            try:
                int(form.movie_runtime.data)
            except:
                message = "Runtime must be interger!"
                return render_template("user_home.html",items = Movies.query.order_by(Movies.movie_title), user=user, password=password, message=message, form=form)

            new_item = Movies(movie_title=form_movie_title, movie_age=form_movie_age, movie_description=form_movie_description, movie_runtime= form_movie_runtime, movie_cover_art=form_movie_cover_art)

            db.session.add(new_item)
            db.session.commit()

            message = "Item added"
            return render_template("user_home.html",items = Movies.query.order_by(Movies.movie_title), user=user, password=password, message=message, form=form)


    return render_template("user_home.html",items = Movies.query.order_by(Movies.movie_title), user=user, password=password, message="", form=form)
   

@app.route("/modify/<movie_id>/<user>", methods=['GET', 'POST'])
def modify_movie(movie_id, user):

    UserAccount = Users.query.filter_by(username=str(user)).first()
    password = UserAccount.password

    item_to_modify = Movies.query.filter_by(id=movie_id).first()

    form = Modify_Confirm()

    if form.validate_on_submit():
        
        if form.cancel.data:

            return redirect(url_for("logged_in", user=user, password=password))

        elif form.modify.data:

            # Validates form data upon submission, done without route rather than form otherwise would try to validate on ant button press
            # This means that is you wanted to cancel the modification it would try to vaildate but couldnt so would fail
            # Instead it validates on the modift/update button press

            form_movie_title = form.title.data
            form_movie_age = form.movie_age.data
            form_movie_description = form.movie_description.data
            form_movie_runtime = form.movie_runtime.data
            form_movie_cover_art = form.movie_cover_art.data

            if not form_movie_cover_art:
                message = "Empty movie cover art"
                return render_template("modify.html", form=form, item=item_to_modify, user=user, password=password, message=message)

            if not form_movie_title:
                message = "Empty movie title"
                return render_template("modify.html", form=form, item=item_to_modify, user=user, password=password, message=message)
            
            if not form_movie_age:
                message = "Empty movie age - rating"
                return render_template("modify.html", form=form, item=item_to_modify, user=user, password=password, message=message)   
            
            if not form_movie_description:
                message = "Empty movie description"
                return render_template("modify.html", form=form, item=item_to_modify, user=user, password=password, message=message)

            if not form_movie_runtime:
                message = "Empty movie runtime"
                return render_template("modify.html", form=form, item=item_to_modify, user=user, password=password, message=message)
            
            try:
                int(form.movie_runtime.data)
            except:
                message = "Runtime must be interger!"
                return redirect("user_home.html",items = Movies.query.order_by(Movies.movie_title), user=user, password=password, message=message, form=form)

            item_to_modify.movie_cover_art = form.movie_cover_art.data
            item_to_modify.movie_title = form.movie_title.data
            item_to_modify.movie_age = form.movie_age.data
            item_to_modify.movie_description = form.movie_description.data
            item_to_modify.runtime = form.movie_runtime.data

            db.session.commit()

            message = "Updated"
            return render_template("modify.html", form=form, item=item_to_modify, user=user, password=password, message=message)

            
        elif form.submit.data:
    
            reviews = MovieReviews.query.filter_by(movie_id=movie_id).all()
            
            for review in reviews:
                db.session.delete(review)

            db.session.delete(item_to_modify)
            db.session.commit()
            
            message = f"{item_to_modify.movie_title} Deleted"

            return redirect(url_for("logged_in", user=user, password=password, message=message))

            #return render_template("user_home.html",items = Movies.query.order_by(Movies.movie_title), user=user, password=password, message=f"{item_to_modify.movie_title} Deleted")

    else:

        if user == "" or password == "":
            return render_template("index.html")
    

        item_to_modify = Movies.query.filter_by(id=movie_id).first()
        return render_template("modify.html", form=form, item=item_to_modify, user=user, password=password, message="")