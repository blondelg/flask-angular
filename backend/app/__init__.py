import click
from flask import Flask
from app.config import Config
from flask_migrate import Migrate
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    return app


def init_db():
    db.drop_all()
    db.create_all()


@click.command("init-db")
@with_appcontext
def init_db_command():
    """Clear existing data and create new tables."""
    init_db()
    click.echo("Initialized the database.")


app = create_app()
if __name__ == "__main__":
    print('RUN')
    app = create_app()
    app.run(host='0.0.0.0')

from app import models
from app.routes import api


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'api': api, 'models': models}
