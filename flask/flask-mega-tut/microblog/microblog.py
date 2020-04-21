# initialize app's __init__.py file by importing it
from app import app, db
from app.models import User, Post

# now when we run `flask shell`, this is the context
@app.shell_context_processor
def make_shell_context():
    return {"db": db, "User": User, "Post": Post}
