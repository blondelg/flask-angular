from flask import Flask
from flask_restful import Resource, Api
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')


from app import routes, models


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'api': api, 'User': models.User}


