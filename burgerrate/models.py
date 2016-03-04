from burgerrate import db


class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    burgerRating = db.Column(db.Float(8))
    sidesRating = db.Column(db.Float(8))
    serviceRating = db.Column(db.Float(8))
    overallRating = db.Column(db.Float(8))
    isFinal = db.Column(db.Boolean())

    def __init__(self, name, burgerRating, sidesRating, drinksRating, overallRating):
        self.name = name
        self.burgerRating = burgerRating
        self.sidesRating = sidesRating
        self.drinksRating = drinksRating
        self.overallRating = overallRating
        self.isFinal = False

    def __repr__(self):
        return self.name

    def setFinalState(self, state):
        self.isFinal = state
        return self.isFinal

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
