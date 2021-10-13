from flask import Flask
from app.config import Config
from app.db import get_db
from flask_migrate import Migrate


db = get_db()
migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    return app


app = create_app()
if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0')

from app import models
from app.routes import api


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'api': api, 'models': models}
