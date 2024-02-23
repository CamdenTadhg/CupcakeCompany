"""Flask app for Cupcakes"""
from flask import Flask, render_template, request, jsonify
from models import db, connect_db, Cupcake
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

@app.route('/')
def show_homepage():
    return render_template('home.html')

@app.route('/api/cupcakes')
def show_cupcakes():
    all_cupcakes = db.session.execute(db.select(Cupcake)).scalars()
    serialized_cupcakes = [cupcake.serialize_cupcake() for cupcake in all_cupcakes]

    return jsonify(cupcakes = serialized_cupcakes)

@app.route('/api/cupcakes/<int:id>')
def show_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)

    return jsonify(cupcake = cupcake.serialize_cupcake())

@app.route('/api/cupcakes', methods=["POST"])
def add_cupcake():
    flavor = request.json['flavor']
    size = request.json['size']
    rating = request.json['rating']
    image = request.json.get('image')
    new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)
    db.session.add(new_cupcake)
    db.session.commit()

    return (jsonify(cupcake = new_cupcake.serialize_cupcake()), 201)

@app.route('/api/cupcakes/<int:id>', methods=["PATCH"])
def update_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.image = request.json.get('image', cupcake.image)
    db.session.commit()

    return jsonify(cupcake = cupcake.serialize_cupcake())

@app.route('/api/cupcakes/<int:id>', methods=["DELETE"])
def delete_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message="cupcake deleted")



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