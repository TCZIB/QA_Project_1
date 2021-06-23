from sub_programs import app, db
from flask import render_template, request, url_for
from sub_programs.models import Movies

@app.route("/")
@app.route("/home")

def home_page():
    return render_template('index.html')

@app.route("/movies")
def view_movies():
    return render_template('movies.html', items = Movies.query.all())

@app.route("/movies/reviews/<movie_id>", methods=['GET', 'POST'])
def movie_reviews(movie_id):
    return movie_id