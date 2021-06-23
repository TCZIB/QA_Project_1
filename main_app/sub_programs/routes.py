from sub_programs import models
from sub_programs import app, db
from flask import render_template, request, url_for
from sub_programs.models import Movies, MovieReviews, ReviewLikes 

@app.route("/")
@app.route("/home")

def home_page():
    return render_template('index.html')

@app.route("/movies")
def view_movies():
    return render_template('movies.html', items = Movies.query.all())

@app.route("/movies/reviews/<movie_title>/<movie_id>", methods=['GET', 'POST'])
def movie_reviews_page(movie_title, movie_id):
    
    selected_movie = Movies.query.get(int(movie_id))
    number_of_reviews = 5

    try:
        selected_movie.movie_title
    except:
        return render_template("not_found.html")

    try:
        reviews = MovieReviews.query.filter_by(movie_id=int(selected_movie.id)).all()

    except:
        reviews = 0

    return render_template("review_page.html", item=selected_movie, number_of_reviews=number_of_reviews, reviews=reviews)

@app.route("/not_recognised")
def not_recognised():
    return render_template("not_found.html")