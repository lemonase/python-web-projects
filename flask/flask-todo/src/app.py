#!/usr/bin/env python3
import os

from flask import (Flask, redirect, render_template, request, url_for)
from flask_sqlalchemy import SQLAlchemy

# initialize flask app
app = Flask(__name__)

# configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# intialize db
db = SQLAlchemy(app)


# todo Model
class Todo(db.Model):
    """ Todo list tasks"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)


# routes
@app.route('/')
@app.route('/list')
@app.route('/list/')
def index():
    """ Root Route """
    todo_list = Todo.query.all()
    return render_template('base.html', todo_list=todo_list)


@app.route('/add', methods=["POST"])
def add():
    title = request.form.get("title")
    new = Todo(title=title, complete=False)
    db.session.add(new)
    db.session.commit()
    return redirect(url_for("index"))


@app.route('/update/<int:todo_id>')
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("index"))


@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
