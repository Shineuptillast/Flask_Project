from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager




app = Flask(__name__)  # creating the Flask class object
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///market.db"
db = SQLAlchemy(app)    # creating a sqlalchemy database

app.secret_key='c2e6aeb3057b3fea610efab4'   # for security reasons because the clients will be inserting the data into the database
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = "login_page" # Redirecting to login page
login_manager.login_message_category="info"
from market import routes

