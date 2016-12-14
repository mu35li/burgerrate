from flask_wtf import Form
from wtforms import StringField, SelectField, validators

class RatingForm(Form):
    ratingNumbers = [('0', '0'), ('1', '1'),('2', '2'),('3', '3'),('4', '4'),('5', '5'),('6', '6'),('7', '7'),('8', '8'),('9', '9'),('10', '10')]
    offerRating = SelectField('Menu', choices = ratingNumbers)
    waiterRating = SelectField('Waiter', choices = ratingNumbers)
    athmosphereRating = SelectField('Athmosphere', choices = ratingNumbers)
    burgerName = StringField('Burger Name', [validators.DataRequired()])
    meatRating = SelectField('Meat', choices = ratingNumbers)
    sauceRating = SelectField('Sauce', choices = ratingNumbers)
    burgerQualityRating = SelectField('Quality', choices = ratingNumbers)
    sideName = StringField('Side Name', [validators.DataRequired()])    
    sidesQualityRating = SelectField('Quality', choices = ratingNumbers)
    sidesQuantityRating = SelectField('Quantity', choices = ratingNumbers)

class RestaurantForm(Form):
    restaurantName = StringField('Restaurant Name')