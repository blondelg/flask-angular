from flask import request, jsonify, make_response
from functools import wraps
import jwt


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        # return 401 if token is not passed
        if not token:
            return make_response(jsonify({'message': 'Token is missing !!'}), 401)

        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = User.query \
                .filter_by(public_id=data['public_id']) \
                .first()
        except:
            return make_response(jsonify({'message': 'Token is invalid !!'}), 401)
        # returns the current logged in users contex to the routes
        return f(current_user, *args, **kwargs)

    return decorated
