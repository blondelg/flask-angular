## Flask - Angular project template


### Backend
#### Virtual environnement and dependencies (from .../backend)
```
# Create virtuale environment for backend
python3 -m venv backend/venv

# Activate venv
source backend/venv/bin/activate

# Install Requirements 
pip install -r requirements.txt
```

#### Database (from .../backend)
```
# Create migration direcory
flask db init

# Create migrations
flask db migrate

# Migrate
flask db upgrade

# Migrate forewards
flask db downgrade
```

#### Start and shell (from .../backend)
```
# Run server
export FLASK_APP=app
export FLASK_ENV=development
flask run

# Run shell
flask shell
```

### Frontend

### Sources
https://realpython.com/token-based-authentication-with-flask/
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins
https://www.geeksforgeeks.org/using-jwt-for-user-authentication-in-flask/