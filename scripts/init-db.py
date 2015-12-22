import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from people import db
from people.models import User, Notification
from werkzeug.security import generate_password_hash
import time

db.drop_all()
db.create_all()

ts = time.time()

user = User("00admin", "Admin", "Account", generate_password_hash("plaintextpassword"),ts)
user.active = True
user.confirmed_at = ts

notification = Notification("Info", ts, "Hello People", "Test notification", None, user)
notification2 = Notification("Warning", ts, "Important message!!!", "This is a very important message.", user, user)

db.session.add(user)
db.session.add(notification)
db.session.add(notification2)

db.session.commit()
