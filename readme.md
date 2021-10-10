# Create virtuale environment for backend
python3 -m venv backend/venv

# Activate venv
source backend/venv/bin/activate

# Install Requirements 
pip install -r requirements.txt


# Database
## Create migration direcory
flask db init

## Create migrations
flask db migrate

## Migrate
flask db upgrade

## Migrate forewards
flask db downgrade

# Run shell
flask shell


# Sources
https://realpython.com/token-based-authentication-with-flask/
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins
