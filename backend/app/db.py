from flask_sqlalchemy import SQLAlchemy


def get_db():
    db = SQLAlchemy()
    return db