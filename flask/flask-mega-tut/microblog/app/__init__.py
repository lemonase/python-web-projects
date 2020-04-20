from flask import Flask
from config import Config

# create flask app, passing in filename
app = Flask(__name__)

# combine our config object with flask's
app.config.from_object(Config)

# add routes
from app import routes

