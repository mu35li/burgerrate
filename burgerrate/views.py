from burgerrate import app, db
from burgerrate.forms import RestaurantForm, RatingForm
from burgerrate.models import Rating, Restaurant
from flask import render_template, redirect, url_for

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
        return redirect(url_for("listRestaurants"))
    return render_template('newRestaurant.html', form=restaurantForm)

@app.route("/restaurants")
def listRestaurants(restaurantId=None):
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

@app.route("/admin")
def admin():
    restaurants = Restaurant.query.all()
    return render_template("admin.html", restaurants=restaurants)

@app.route("/restaurants/<restaurantId>", methods=(["GET"]))
def restaurantDetails(restaurantId):
    if restaurantId is not None:
        restaurant = Restaurant.query.get(restaurantId)
        return render_template('restaurantRating.html', restaurant=restaurant)
    else:
        return redirect(url_for("listRestaurants"))

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