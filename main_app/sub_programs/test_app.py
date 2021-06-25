from flask import url_for
from flask_testing import TestCase
import os

# import the app's classes and objects
from sub_programs import app

class TestBase(TestCase):

    def create_app(self):
        # Pass in testing configurations for the app. Here we use sqlite without a persistent database for our tests.
        app.config.update(SQLALCHEMY_DATABASE_URI=os.getenv("databaseLogin"),
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    def setUp(self):
    #  Will be called before every test
        pass

    def tearDown(self):
    #   Will be called after every test
        pass

    def test_home_get(self):

        response = self.client.get(url_for('home_page'))
        self.assertEqual(response.status_code, 200)
    
    def test_home_get(self):

        response = self.client.get(url_for('view_movies'))
        self.assertEqual(response.status_code, 200)

    def test_home_get(self):

        response = self.client.get(url_for('login_page'))
        self.assertEqual(response.status_code, 200)