from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# create flask app, passing in filename
app = Flask(__name__)

# combine our config object with flask's
app.config.from_object(Config)

# bring in database object and migration
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# create login manager
login = LoginManager(app)
login.login_view = "login"  # set to the url_for() login endpoint

# add routes
from app import routes, models
