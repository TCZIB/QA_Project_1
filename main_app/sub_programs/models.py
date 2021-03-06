from sub_programs import db

class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    movie_title = db.Column(db.String(1000), nullable=False)
    movie_age = db.Column(db.String(1000), nullable=False)
    movie_description = db.Column(db.String(1000), nullable=False)
    movie_runtime = db.Column(db.Integer(), nullable=False)
    movie_cover_art = db.Column(db.String(500))

    reviews = db.relationship('MovieReviews', backref="movie")

class MovieReviews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'), nullable=False)
    
    review_contents = db.Column(db.String(500), nullable=False)
    review_author = db.Column(db.String(30), nullable=False)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)
