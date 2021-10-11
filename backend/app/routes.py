from flask_restful import Api
from app import app
from app.views import HelloWorld, Login, Signup



api = Api(app)

api.add_resource(HelloWorld, '/')
api.add_resource(Signup, '/signup')
api.add_resource(Login, '/login')