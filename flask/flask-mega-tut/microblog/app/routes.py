from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'james'}
    posts = [
            {
                'author': {'username': 'john'},
                'body': 'Beautiful day here in chicago!'
            },
            {
                'author': {'username': 'billy'},
                'body': 'I like turtles'
            }
    ]

    return render_template('index.html', title="Home", user=user, posts=posts)

