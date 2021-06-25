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