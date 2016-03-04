from flask import Flask, render_template, redirect, url_for

from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_pyfile("../config.py")

db = SQLAlchemy(app)


import burgerrate.views
import burgerrate.forms
import burgerrate.models





