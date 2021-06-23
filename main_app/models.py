from sub_programs import db

class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_title = db.Column(db.String(30), nullable=False)
    movie_age = db.Column(db.String(30), nullable=False)
    movie_description = db.Column(db.String(500), nullable=False)
    movie_runtime = db.Column(db.Integer(), nullable=False)

    Movie_Reviews = db.relationship('movies', backref='movie')

class Movie_Reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'))
    review_contents = db.Column(db.String(500), nullable=False)
    review_author = db.Column(db.String(30), nullable=False)

    Review_Likes = db.relationship('Review_Likes', backref='movie_review')
    
class Review_Likes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_review_id = db.Column(db.Integer, db.ForeignKey('Movie_Reviews.id'))
    food_item = db.Column(db.Integer, db.ForeignKey('food_items.id'))
    meals_rel = db.relationship('Food_Items', backref='Meal_Contents')
