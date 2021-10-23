from flask_restful import Api
from app import app
from app.views import Hello, Login, Signup



api = Api(app)

api.add_resource(Hello, '/')
api.add_resource(Signup, '/signup')
api.add_resource(Login, '/login')