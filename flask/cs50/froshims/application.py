import sqlite3

from flask import Flask, redirect, render_template, request

app = Flask(__name__)

SPORTS = ["Dodgeball", "Football", "Soccer", "Frisbee"]

# db using sqlite3 library instead of cs50
conn = sqlite3.connect("froshims.db", check_same_thread=False)
cur = conn.cursor()

# create database if it doesn't exist
cur.execute(
    """
    CREATE TABLE IF NOT EXISTS registrants (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        sport TEXT NOT NULL
    )
    """
)

@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    sport = request.form.get("sport")

    if not name:
        return render_template("failure.html", error="No name submitted")
    if sport not in SPORTS:
        return render_template("failure.html", error="Incorrect sport submitted")

    cur.execute("INSERT INTO registrants (name, sport) VALUES (?,?)", (name, sport))
    conn.commit()

    return redirect("/registrants")


@app.route("/registrants")
def registrants():
    registrants = cur.execute("SELECT * FROM registrants")
    return render_template("success.html", registrants=registrants)
