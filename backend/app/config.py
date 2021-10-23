import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = "#d#JCqTTW\nilK\\7m\x0bp#\tj~#H"

    # DB
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # JWT
    JWT_EXPIRATION_TIME = 30


class TestConfig(object):
    TESTING = True
    SECRET_KEY = "#d#JCqTTW\nilK\\7m\x0bp#\tj~#H"

    # DB
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # JWT
    JWT_EXPIRATION_TIME = 30



