import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from burgerrate import db
from burgerrate.models import Restaurant, Rating

db.drop_all()
db.create_all()
