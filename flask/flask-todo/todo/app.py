import os
import json
from datetime import datetime

from flask import Flask, Response, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    """ Default Route """
    return "<h1>Hello Mate</h1>"


@app.route('/api/v1', methods=["GET"])
def info_view():
    """List of routes for this API."""
    output = {
        'info': 'GET /api/v1',
        'register': 'POST /api/v1/accounts',
        'single profile detail': 'GET /api/v1/accounts/<username>',
        'edit profile': 'PUT /api/v1/accounts/<username>',
        'delete profile': 'DELETE /api/v1/accounts/<username>',
        'login': 'POST /api/v1/accounts/login',
        'logout': 'GET /api/v1/accounts/logout',
        "user's tasks": 'GET /api/v1/accounts/<username>/tasks',
        "create task": 'POST /api/v1/accounts/<username>/tasks',
        "task detail": 'GET /api/v1/accounts/<username>/tasks/<id>',
        "task update": 'PUT /api/v1/accounts/<username>/tasks/<id>',
        "delete task": 'DELETE /api/v1/accounts/<username>/tasks/<id>'
    }
    return jsonify(output)


@app.route('/api/v1/accounts/<username>/tasks', methods=['POST'])
def create_task(username):
    """ Creates a task for the user """
    user = User.query.filter_by(username=username).first()
    if user:
        task = Task(
            name=request.form['name'],
            note=request.form['note'],
            creation_date=datetime.now(),
            due_date=datetime.strptime(due_date, INCOMING_DATE_FMT)
            if due_date else None,
            completed=bool(requst.form['completed']),
            user_id=user.id,
        )
        db.seesion.add(task)
        db.session_commit()
        output = {'msg', 'posted'}
        response = Response(mimetype="application/json",
                            response=json.dumps(output),
                            status=201)
        return response
