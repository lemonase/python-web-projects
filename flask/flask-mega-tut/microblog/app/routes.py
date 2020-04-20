from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'james'}
    return render_template('index.html', title="Home", user=user)
    # return """ <h1> Hello """ + user['username'] + """ </h1> """

