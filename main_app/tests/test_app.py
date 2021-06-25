from flask_testing import TestCase

class TestBase(TestCase):

    def create_app(self):
    # Pass in configurations for tests
        pass

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