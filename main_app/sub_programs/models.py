from sub_programs import db

class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    movie_title = db.Column(db.String(30), nullable=False)
    movie_age = db.Column(db.String(30), nullable=False)
    movie_description = db.Column(db.String(500), nullable=False)
    movie_runtime = db.Column(db.Integer(), nullable=False)
    movie_cover_art = db.Column(db.String(100))

    reviews = db.relationship('Movie_Reviews', backref="movie")

class Movie_Reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'), nullable=False)
    
    review_contents = db.Column(db.String(500), nullable=False)
    review_author = db.Column(db.String(30), nullable=False)

    review_likes = db.relationship('Review_Likes', backref="movie_review")

class Review_Likes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_review_id = db.Column(db.Integer, db.ForeignKey('movie_reviews.id'))
    
    like_status = db.Column(db.Boolean)
    like_user = db.Column(db.String(15), nullable=False)
