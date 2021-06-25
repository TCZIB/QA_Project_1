from typing_extensions import final
from sub_programs.forms import Movie_Review_Form, Login_Form, Modify_Confirm
from sub_programs import models
from sub_programs import app, db
from flask import render_template, request, url_for, redirect
from sub_programs.models import Movies, MovieReviews, Users
from sub_programs import profanities, accepted_ages
import random

@app.route("/")
@app.route("/home")

def home_page():

    all_movies = Movies.query.all()
    ordered_list = []

    for movie in all_movies:
        ordered_list.append(movie.id)

    Random_Movies = True
    attempt = 0
    items = []
    final_list = []

    while Random_Movies:
        
        attempt += 1
        random_movie = random.choice(ordered_list)
        
        if random_movie not in final_list:
            
            final_list.append(random_movie)
            items.append(Movies.query.get(int(random_movie)))
        
        if len(final_list) == 5:
            Random_Movies = False

        if attempt == 100:
            Random_Movies = False


    return render_template('index.html', items=items)

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

    # Again, validating outside of form to make my life easier, it means i dont have to code the same thing twice to display a message to the user

    if form.validate_on_submit():

        print(1)

        review_content = form.review.data
        review_author = form.username.data

        review_content_test = review_content.split()

        has_already_reviwed = MovieReviews.query.filter_by(review_author=review_author).all()

        for review in has_already_reviwed:
            if review.review_contents == review_content:
                message = "You've already submitted this review!"
                return render_template("review_page.html", item=selected_movie, reviews=reviews, MovieReviews=MovieReviews, form=form, message=message)

        for word in review_content_test:
            for bad_word in profanities:
                if word == bad_word:
                    message = f"Word {word.upper()} Not allowed!"
                    return render_template("review_page.html", item=selected_movie, reviews=reviews, MovieReviews=MovieReviews, form=form, error_message=message)

        if len(review_author) <= 4 or len(review_author) >= 31:
            message = "Please use a username between 5-30 characters"
            return render_template("review_page.html", item=selected_movie, reviews=reviews, MovieReviews=MovieReviews, form=form, error_message=message)

        new_review = MovieReviews(movie_id=selected_movie.id, review_contents=review_content, review_author=review_author)

        db.session.add(new_review)
        db.session.commit()

        return redirect(url_for("movie_reviews_page", movie_title=movie_title, movie_id=selected_movie.id))

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
                return render_template("user_home.html",items = Movies.query.order_by(Movies.movie_title), user=user, password=password, message_add_error=message, form=form)
            
            try:
                int(form.movie_runtime.data)
            except:
                message = "Runtime must be interger!"
                return render_template("user_home.html",items = Movies.query.order_by(Movies.movie_title), user=user, password=password, message_add_error=message, form=form)

            new_item = Movies(movie_title=form_movie_title, movie_age=form_movie_age, movie_description=form_movie_description, movie_runtime= form_movie_runtime, movie_cover_art=form_movie_cover_art)

            if form_movie_age not in accepted_ages:
                message = "Incorrect age ranges"
                return render_template("user_home.html",items = Movies.query.order_by(Movies.movie_title), user=user, password=password, message_add_error=message, form=form)

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

            form_movie_title = form.movie_title.data
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
                return render_template("modify.html", form=form, item=item_to_modify, user=user, password=password, message=message)

            if form_movie_age not in accepted_ages:
                message = "Incorrect age ranges"
                return render_template("modify.html", form=form, item=item_to_modify, user=user, password=password, message=message)

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