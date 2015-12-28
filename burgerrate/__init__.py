from flask import Flask, render_template, redirect, url_for
from flask_wtf import Form
from wtforms import StringField, SelectField
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_pyfile("../config.py")

db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/new", methods=(["GET", "POST"]))
def newRestaurant():
    restaurantForm = RestaurantForm()
    if restaurantForm.validate_on_submit():
        restaurant = Restaurant(restaurantForm.restaurantName.data, None, None, None, None)
        db.session.add(restaurant)
        db.session.commit()
        return render_template('index.html')
    return render_template('newRestaurant.html', form=restaurantForm)

@app.route("/restaurants")
def listRestaurants():
    restaurants = Restaurant.query.all()
    return render_template('restaurantList.html', restaurants=restaurants)

@app.route("/addRating/<restaurantId>", methods=(["GET", "POST"]))
def addRating(restaurantId):
    restaurant = Restaurant.query.get(restaurantId)
    ratingForm = RatingForm()
    if ratingForm.validate_on_submit():

        rating = Rating(restaurant.id, ratingForm.burgerName.data, 
            int(ratingForm.meatRating.data), 
            int(ratingForm.sauceRating.data), 
            int(ratingForm.burgerQualityRating.data), 
            ratingForm.sideName.data, 
            int(ratingForm.sidesQualityRating.data), 
            int(ratingForm.sidesQuantityRating.data), 
            int(ratingForm.offerRating.data), 
            int(ratingForm.waiterRating.data), 
            int(ratingForm.athmosphereRating.data))
        db.session.add(rating)
        db.session.commit()

        success = updateRestaurant(restaurant)
        if success:
            return redirect(url_for("listRestaurants"))

    return render_template("addRating.html", form=ratingForm, restaurant=restaurant)
    
def updateRestaurant(restaurant):
    ratings = Rating.query.filter_by(restaurantId=restaurant.id).all()
    restaurant = Restaurant.query.get(restaurant.id)
    offerRating = 0
    offerCount = 0
    waiterRating = 0
    waiterCount = 0
    athmosphereRating = 0
    athmosphereCount = 0
    meatRating = 0
    meatCount = 0
    sauceRating = 0
    sauceCount = 0
    burgerQualityRating = 0
    burgerQualityCount = 0
    sidesQualityRating = 0
    sidesQualityCount = 0
    sidesQuantityRating = 0
    sidesQuantityCount = 0

    for rating in ratings:
        offerRating += rating.offerRating
        offerCount+= 1
        waiterRating += rating.waiterRating
        waiterCount += 1
        athmosphereRating += rating.athmosphereRating
        athmosphereCount += 1
        meatRating += rating.meatRating
        meatCount+= 1
        sauceRating += rating.sauceRating
        sauceCount+= 1
        burgerQualityRating += rating.burgerQualityRating
        burgerQualityCount+= 1
        sidesQualityRating += rating.sidesQualityRating
        sidesQualityCount+= 1
        sidesQuantityRating += rating.sidesQuantityRating
        sidesQuantityCount+= 1

    offerRating = offerRating/offerCount
    waiterRating = waiterRating/waiterCount
    athmosphereRating = athmosphereRating/athmosphereCount
    meatRating = meatRating/meatCount
    sauceRating = sauceRating/sauceCount
    burgerQualityRating = burgerQualityRating/burgerQualityCount
    sidesQualityRating = sidesQualityRating/sidesQualityCount
    sidesQuantityRating = sidesQuantityRating/sidesQuantityCount

    burgerRating = (meatRating+sauceRating+burgerQualityRating)/3
    sidesRating = (sidesQuantityRating+sidesQualityRating)/2
    serviceRating = (athmosphereRating+offerRating*2+waiterRating)/4
    overallRating = (burgerRating*2+sidesRating+serviceRating)/4

    restaurant.burgerRating = burgerRating
    restaurant.serviceRating = serviceRating
    restaurant.sidesRating = sidesRating
    restaurant.overallRating = overallRating

    db.session.commit()

    return True


class RatingForm(Form):
    ratingNumbers = [('0', '0'), ('1', '1'),('2', '2'),('3', '3'),('4', '4'),('5', '5'),('6', '6'),('7', '7'),('8', '8'),('9', '9'),('10', '10')]
    offerRating = SelectField('Offer', choices = ratingNumbers)
    waiterRating = SelectField('Waiter', choices = ratingNumbers)
    athmosphereRating = SelectField('Athmosphere', choices = ratingNumbers)
    burgerName = StringField('Burger Name')
    meatRating = SelectField('Meat', choices = ratingNumbers)
    sauceRating = SelectField('Sauce', choices = ratingNumbers)
    burgerQualityRating = SelectField('Quality', choices = ratingNumbers)
    sideName = StringField('Side Name')    
    sidesQualityRating = SelectField('Quality', choices = ratingNumbers)
    sidesQuantityRating = SelectField('Quantity', choices = ratingNumbers)

class RestaurantForm(Form):
    restaurantName = StringField('Restaurant Name')

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    burgerRating = db.Column(db.Float(8))
    sidesRating = db.Column(db.Float(8))
    serviceRating = db.Column(db.Float(8))
    overallRating = db.Column(db.Float(8))

    def __init__(self, name, burgerRating, sidesRating, drinksRating, overallRating):
        self.name = name
        self.burgerRating = burgerRating
        self.sidesRating = sidesRating
        self.drinksRating = drinksRating
        self.overallRating = overallRating

    def __repr__(self):
        return self.name

class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    restaurantId = db.Column(db.Integer)
    burgerName = db.Column(db.String(80))
    meatRating = db.Column(db.Integer)
    sauceRating = db.Column(db.Integer)
    burgerQualityRating = db.Column(db.Integer)
    sideName = db.Column(db.String(80))
    sidesQualityRating = db.Column(db.Integer)
    sidesQuantityRating = db.Column(db.Integer)
    offerRating = db.Column(db.Integer)
    waiterRating = db.Column(db.Integer)
    athmosphereRating = db.Column(db.Integer)

    def __init__(self, restaurantId, burgerName, meatRating, sauceRating, burgerQualityRating, sideName, sidesQualityRating, sidesQuantityRating, offerRating, waiterRating, athmosphereRating):
        print('init')
        self.restaurantId = restaurantId
        self.burgerName = burgerName
        self.meatRating = meatRating
        self.sauceRating = sauceRating
        self.burgerQualityRating = burgerQualityRating
        self.sideName = sideName
        self.sidesQualityRating = sidesQualityRating
        self.sidesQuantityRating = sidesQuantityRating
        self.offerRating = offerRating
        self.waiterRating = waiterRating
        self.athmosphereRating = athmosphereRating
        print('init finished')

    def __repr__(self):
        return self.restaurantId
