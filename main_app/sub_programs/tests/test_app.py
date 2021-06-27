from flask import url_for
from flask_testing import TestCase
import os
from sub_programs import db
from sub_programs.models import Movies, MovieReviews, Users
import os
import csv

# import the app's classes and objects
from sub_programs import app

global_testing_variables_good = dict(movie_cover_art="Something.html", movie_title="test", movie_age="PG", movie_description="Something cool", movie_runtime=105)
global_testing_variables_no_age = dict(movie_cover_art="Something.html", movie_title="test", movie_age="", movie_description="Something cool", movie_runtime=105)
global_testing_variables_no_cover = dict(movie_cover_art="", movie_title="test", movie_age="PG", movie_description="Something cool", movie_runtime=105)
global_testing_variables_no_title = dict(movie_cover_art="Something.html", movie_title="", movie_age="PG", movie_description="Something cool", movie_runtime=105)
global_testing_variables_no_description = dict(movie_cover_art="Something.html", movie_title="test", movie_age="PG", movie_description="", movie_runtime=105)
global_testing_variables_no_runtime = dict(movie_cover_art="Something.html", movie_title="test", movie_age="PG", movie_description="Something cool", movie_runtime="")
global_testing_variables_bad_age = dict(movie_cover_art="Something.html", movie_title="test", movie_age="boo", movie_description="Something cool", movie_runtime=105)
global_testing_variables_bad_runtime = dict(movie_cover_art="Something.html", movie_title="test", movie_age="PG", movie_description="Something cool", movie_runtime="hello")

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

        db.drop_all()
        db.create_all()

        new_movie_item = Movies(movie_title="Shrek", movie_age="U", movie_description="Something about shrek", movie_runtime="105", movie_cover_art="Some cover art")
        db.session.add(new_movie_item)
        db.session.commit()

        new_review_item = MovieReviews(movie_id=1, review_contents="somthing", review_author="i am a test user")
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
    
    def test_login_no_user(self):

        response = self.client.post(
            url_for('login_page'),
            data = dict(form_username="efhsdjf", form_password="sfsdf"),
            follow_redirects=True
        )

        self.assertIn(b'User not found', response.data)

    def test_login_incorrect_password(self):

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
    
    def test_add_movie_success(self):

        response = self.client.post(
            url_for('logged_in', user="zib", password="zib"),
            data = global_testing_variables_good,
            follow_redirects=True
        )

        self.assertIn(b'Item added', response.data)
    
    def test_add_movie_no_cover(self):

        response = self.client.post(
            url_for('logged_in', user="zib", password="zib"),
            data = global_testing_variables_no_cover,
            follow_redirects=True
        )

        self.assertIn(b'Empty movie cover photo', response.data)

    def test_add_movie_no_title(self):

        response = self.client.post(
            url_for('logged_in', user="zib", password="zib"),
            data = global_testing_variables_no_title,
            follow_redirects=True
        )

        self.assertIn(b'Empty movie title', response.data)

    def test_add_movie_no_age_rating(self):

        response = self.client.post(
            url_for('logged_in', user="zib", password="zib"),
            data = global_testing_variables_no_age,
            follow_redirects=True
        )

        self.assertIn(b'Empty movie age - rating', response.data)
        
    def test_add_movie_bad_age(self):

        response = self.client.post(
            url_for('logged_in', user="zib", password="zib"),
            data = global_testing_variables_bad_age,
            follow_redirects=True
        )

        self.assertIn(b'Incorrect age ranges', response.data)

    def test_add_movie_no_description(self):

        response = self.client.post(
            url_for('logged_in', user="zib", password="zib"),
            data = global_testing_variables_no_description,
            follow_redirects=True
        )

        self.assertIn(b'Empty movie description', response.data)

    def test_add_movie_no_runtime(self):

        response = self.client.post(
            url_for('logged_in', user="zib", password="zib"),
            data = global_testing_variables_no_runtime,
            follow_redirects=True
        )

        self.assertIn(b'Empty movie runtime', response.data)

    def test_add_movie_no_runtime(self):

        response = self.client.post(
            url_for('logged_in', user="zib", password="zib"),
            data = global_testing_variables_bad_runtime,
            follow_redirects=True
        )

        self.assertIn(b'Runtime must be interger!', response.data)