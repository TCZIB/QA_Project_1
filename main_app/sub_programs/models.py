from sub_programs import db

class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    movie_title = db.Column(db.String(30), nullable=False)
    movie_age = db.Column(db.String(30), nullable=False)
    movie_description = db.Column(db.String(500), nullable=False)
    movie_runtime = db.Column(db.Integer(), nullable=False)
    movie_cover_art = db.Column(db.String(100))

    reviews = db.relationship('MovieReviews', backref="movie")

class MovieReviews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'), nullable=False)
    
    review_contents = db.Column(db.String(500), nullable=False)
    review_author = db.Column(db.String(30), nullable=False)


class ReviewLikes(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    review_id = db.Column(db.Integer, db.ForeignKey('movie_reviews.id'), nullable=False)

    like_bool = db.Column(db.Boolean())
    like_author = db.Column(db.String(30), nullable=False)
