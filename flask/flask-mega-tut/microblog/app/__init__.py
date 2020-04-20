from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# create flask app, passing in filename
app = Flask(__name__)

# combine our config object with flask's
app.config.from_object(Config)

# bring in database object and migration
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# add routes
from app import routes, models

