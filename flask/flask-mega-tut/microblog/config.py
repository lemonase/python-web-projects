"""
Class that extends flask config and can be extended itself
"""

import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """ Custom config with relevant configs """
    SECRET_KEY = os.environ.get("SECRET_KEY") or "yikes"

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_RUL"
    ) or "sqlite:///" + os.path.join(BASEDIR, "app.db")
    SQLALCHEMY_TRACK_NOTIFICATIONS = False
