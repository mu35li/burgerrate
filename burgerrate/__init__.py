from flask import Flask, render_template
from flask_wtf import Form
from wtforms import StringField
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_pyfile("../config.py")

db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/new")
def newRating():
    ratingForm = RatingForm()
    return render_template('newRating.html', form=ratingForm)
@app.route("/save", methods=(['POST']))
def saveRating():
    ratingForm = RatingForm()
    if ratingForm.validate_on_submit():
        restaurant = Restaurant(ratingForm.restaurantName.data)
        db.session.add(restaurant)
        db.session.commit()
        return render_template('index.html')
    return render_template('newRating.html')


class RatingForm(Form):
    restaurantName = StringField('Restaurant Name')

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name
