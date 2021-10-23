import flask_unittest
from app import create_app
from app.config import TestConfig
import os
import tempfile




class TestApi(flask_unittest.AppTestCase):

    def create_app(self):
        self.config = TestConfig
        self.config.db_fd, self.config.SQLALCHEMY_DATABASE_URI = tempfile.mkstemp()

        app = create_app(config_class=self.config)
        yield app

    def setUp(self, app):
        # Perform set up before each test, using app
        pass
        

    def tearDown(self, app):
        # Perform tear down after each test, using app
        os.close(self.config.db_fd)
        os.unlink(self.config.SQLALCHEMY_DATABASE_URI)

    def test_test(self, app):
        self.assertTrue(True)