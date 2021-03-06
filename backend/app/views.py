from app import models
from app import app, db
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from flask import jsonify, make_response, request
from flask_restful import Resource
from datetime import datetime, timedelta
import jwt

from app.utils import token_required


class Hello(Resource):
    def get(self):
        return {'hello': 'world'}


class Login(Resource):
    def post(self):
        # creates dictionary of form data
        auth = request.form

        if not auth or not auth.get('username') or not auth.get('password'):
            # returns 401 if any email or / and password is missing
            return make_response(
                'Could not verify',
                401,
                {'WWW-Authenticate': 'Basic realm ="Login required !!"'}
            )

        user = models.User.query.filter_by(username=auth.get('username')).first()

        if not user:
            # returns 401 if user does not exist
            return make_response(
                'Could not verify',
                401,
                {'WWW-Authenticate': 'Basic realm ="User does not exist !!"'}
            )

        if check_password_hash(user.password_hash, auth.get('password')):
            # generates the JWT Token
            token = jwt.encode({
                'public_id': user.public_id,
                'exp': datetime.utcnow() + timedelta(minutes=app.config['JWT_EXPIRATION_TIME'])
            }, app.config['SECRET_KEY'])

            return make_response(jsonify({'token': token}), 201)
        # returns 403 if password is wrong
        return make_response(
            'Could not verify',
            403,
            {'WWW-Authenticate': 'Basic realm ="Wrong Password !!"'}
        )


# signup route
class Signup(Resource):
    def post(self):
        # creates a dictionary of the form data
        data = request.form

        # gets name, email and password
        username = data.get('username')
        password = data.get('password')

        # checking for existing user
        user = models.User.query \
            .filter_by(username=username) \
            .first()
        if not user:
            # database ORM object
            user = models.User(
                public_id=str(uuid.uuid4()),
                username=username,
                password_hash=generate_password_hash(password)
            )
            # insert user
            db.session.add(user)
            db.session.commit()

            return make_response('Successfully registered.', 201)
        else:
            # returns 202 if user already exists
            return make_response('User already exists. Please Log in.', 202)