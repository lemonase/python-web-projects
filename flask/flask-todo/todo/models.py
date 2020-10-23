import secrets
import sys
from datetime import datetime

from todo.app import db


class Task(db.Model):
    """ Todo list tasks"""
    # fields
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode, nullable=False)
    note = db.Column(db.Unicode)
    creation_date = db.Column(db.DateTime, nullable=False)
    due_date = db.Column(db.DateTime)
    completed = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # relationships
    user = db.relationship("user", back_populates="tasks")

    def __init__(self, *args, **kwargs):
        """ Constructor """
        super().__init__(*args, **kwargs)
        self.creation_date = datetime.now()


class User(db.Model):
    """ User model """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Unicode, nullable=False)
    email = db.Column(db.Unicode, nullable=False)
    password = db.Column(db.Unicode, nullable=False)
    date_joined = db.Column(db.DateTime, nullable=False)
    token = db.Column(db.Unicode, nullable=False)

    user = db.relationship("Task", back_populates="user")

    def __init__(self, *args, **kwargs):
        """ Constructor """
        super().__init__(*args, **kwargs)
        self.date_joined = datetime.now()
        self.token = secrets.token_urlsafe(64)
