"""Flask app for Cupcakes"""
from flask import Flask, render_template, request
from models import db, connect_db
from flask_wtf import FlaskForm
from wtforms import StringField
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes_test'
# app.config['SQLALCHEMY_ECHO'] = False
# app.config['TESTING'] = True
app.config['SECRET_KEY'] = "secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

app.app_context().push()

connect_db(app)
db.create_all()








# 21 route for data on all cupcakes
# 20 route for data on single cupcake
# 19 route to create new cupcake
# 18 test routes in Insomnia
# 17 test routes using unittest
# 16 route for updating cupcake
# 15 route for deleting a cupcake
# 14 test new routes in Insomnia
# 13 write tests for new routes
# 12 test routes using unittest
# 11 create homepage
# 10 write javascript for homepage to get cupcakes and submit form
# 9 add tests to ensure 404 is returned when cupcakes don't exist (get/patch/delete)
# 8 add functionality to search for cupcakes (type in term, see newly filtered list of cupcakes)
# 7 refactor javascript code to be object oriented using class methods (fetchAllCupcakes and createCupcakes and instance methods for updating/deleting/searching)
# 6 refactor HTML page to use WTForms (create forms.py too)
# 5 enhance search functionality so it searches as you type
# 4 add functionality on front end to update a cupcake
# 3 add new model/table for ingredients
# 2 allow adding ingredients to each cupcake when adding or editing cupcakes
# 1 create page to add/edit ingredients