from flask import url_for
from flask_testing import TestCase
import os
from sub_programs import db
from sub_programs.models import Movies, MovieReviews, Users
import os
import csv

# import the app's classes and objects
from sub_programs import app

class TestBase(TestCase):

    def create_app(self):
        # Pass in testing configurations for the app. Here we use sqlite without a persistent database for our tests.
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    def setUp(self):

        movie_csv_dir = os.getenv("movie_csv")
        review_csv_dir = os.getenv("review_csv")

        db.drop_all()
        db.create_all()

        movie_csv = csv.reader(open(movie_csv_dir, "r"), delimiter="`")
        review_csv = csv.reader(open(review_csv_dir, "r"), delimiter="`")


        next(movie_csv)
        next(review_csv)

        for row in movie_csv:
            new_movie_item = Movies(movie_title=row[0], movie_age=row[1], movie_description=row[2], movie_runtime=int(row[3]), movie_cover_art=row[4])
            db.session.add(new_movie_item)
            db.session.commit()

        for row in review_csv:
            new_review_item = MovieReviews(movie_id=row[0], review_contents=row[1], review_author=row[2])
            db.session.add(new_review_item)
            db.session.commit()

        moderator = Users(username="moderator", password="moderator")
        zib = Users(username="zib", password="zib")

        db.session.add(moderator)
        db.session.add(zib)
        db.session.commit()

    def tearDown(self):
        db.drop_all()

    def test_home_get(self):

        response = self.client.get(url_for('home_page'))
        self.assertEqual(response.status_code, 200)
    
    def test_view_movies(self):

        response = self.client.get(url_for('view_movies'))
        self.assertEqual(response.status_code, 200)

    def test_login_page(self):

        response = self.client.get(url_for('login_page'))
        self.assertEqual(response.status_code, 200)

    def test_login_sucess(self):

        response = self.client.post(
            url_for('login_page'),
            data = dict(form_username="zib", form_password="zib"),
            follow_redirects=True
        )

        self.assertIn(b'Logout zib', response.data)
    
    def test_login_sucess(self):

        response = self.client.post(
            url_for('login_page'),
            data = dict(form_username="efhsdjf", form_password="sfsdf"),
            follow_redirects=True
        )

        self.assertIn(b'User not found', response.data)

    def test_login_sucess(self):

        response = self.client.post(
            url_for('login_page'),
            data = dict(form_username="zib", form_password="sfsd"),
            follow_redirects=True
        )

        self.assertIn(b'Incorrect password', response.data)

    def test_badword_test(self):

        response = self.client.post(
            url_for('movie_reviews_page', movie_title="shrek", movie_id=1),
            data = dict(username="zib4545", review="shit"),
            follow_redirects=True
        )

        self.assertIn(b'Word SHIT Not allowed!', response.data)

    def test_review_test(self):

        response = self.client.post(
            url_for('movie_reviews_page', movie_title="shrek", movie_id=1),
            data = dict(username="zib", review="Amazing!"),
            follow_redirects=True
        )

        self.assertIn(b'Please use a username between 5-30 characters', response.data)
