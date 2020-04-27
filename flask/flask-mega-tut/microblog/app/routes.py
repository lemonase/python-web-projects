from datetime import datetime

from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

from app import app, db
from app.models import User, Post
from app.forms import LoginForm, RegistrationForm, EditProfileForm


@app.route("/register", methods=["GET", "POST"])
def register():
    # already logged in
    if current_user.is_authenticated:
        return redirect(url_for("index"))

    # grab the form
    form = RegistrationForm()

    # validate data, add to database
    if form.validate_on_submit():
        # create a user object
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)

        # commit to db
        db.session.add(user)
        db.session.commit()

        # keep em moving
        flash("Congratulation, you are now a registered user!")
        return redirect(url_for("login"))

    # return rendered page
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    # user is already logged in
    if current_user.is_authenticated:
        return redirect(url_for("index"))

    form = LoginForm()

    # when the form is submitted
    if form.validate_on_submit():
        # filter and fetch a single user (the first and only) from the database
        user = User.query.filter_by(username=form.username.data).first()

        # login unsuccessful
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for("login"))

        # login successful
        # call login_user from flask_login
        # the user query works because flask_login's user is mixedin in app/models.py
        login_user(user, remember=form.remember_me.data)

        # figure out the next page securely
        next_page = request.args.get("next")
        if not next_page or url_parse(next_page).netloc != "":
            next_page = url_for("index")
        return redirect(next_page)

    return render_template("login.html", title="Sign In", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/user/<username>")
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {"author": {"username": "john"}, "body": "Beautiful day here in chicago!"},
        {"author": {"username": "billy"}, "body": "I like turtles"},
    ]
    return render_template("user.html", user=user, posts=posts)

@app.route("/edit_profile", methods=["GET", "POST"])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash("Your changes have been saved")
        return redirect(url_for("user", username=current_user.username))
    elif request.method == "GET":
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template("edit_profile.html", title='Edit Profile', form=form)


@app.route("/")
@app.route("/index")
@login_required
def index():
    # posts = [
    #     {"author": {"username": "john"}, "body": "Beautiful day here in chicago!"},
    #     {"author": {"username": "billy"}, "body": "I like turtles"},
    # ]
    posts = Post.query.all()

    return render_template("index.html", title="Home", posts=posts)


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()
