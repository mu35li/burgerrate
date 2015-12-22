from flask import Flask, render_template
app = Flask(__name__)

DEBUG = True
SECRET_KEY = "foobar"
SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/people-development.db"
SQLALCHEMY_TRACK_MODIFICATIONS = False


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/new")
def newRating():
	return "new rating incomming"