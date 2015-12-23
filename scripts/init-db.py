import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from burgerrate import db, Restaurant

db.drop_all()
db.create_all()
