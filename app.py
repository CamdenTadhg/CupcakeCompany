"""Flask app for Cupcakes"""
from flask import Flask, render_template, request, jsonify
from models import db, connect_db, Cupcake
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from forms import AddCupcakeForm, UpdateCupcakeForm
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
    addForm = AddCupcakeForm()
    updateForm = UpdateCupcakeForm()
    return render_template('home.html', addForm=addForm, updateForm=updateForm)

@app.route('/api/cupcakes')
def return_cupcakes():
    all_cupcakes = db.session.execute(db.select(Cupcake).order_by(Cupcake.flavor)).scalars()
    serialized_cupcakes = [cupcake.serialize_cupcake() for cupcake in all_cupcakes]

    return jsonify(cupcakes = serialized_cupcakes)

@app.route('/api/cupcakes/<int:id>')
def return_cupcake(id):
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


# 4 create page to add/edit ingredients
    # route
    # form model
    # html page
    # api function to add ingredients
    # axios function to add ingredients
    # api function to update ingredients
    # axios function to update ingredients
# 3 allow adding ingredients to each cupcake when adding cupcakes
# 2 add functionality on front end to update a cupcake
    # update form page
    # route for update form page
    # update axios function
    # fix delete behavior
# 1 add testing (flask & javascript)
# 0 remove logging logic