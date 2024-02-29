"""Flask app for Cupcakes"""
from flask import Flask, render_template, request, jsonify
from models import db, connect_db, Cupcake, Ingredient
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from forms import CupcakeForm, IngredientForm
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
    form = CupcakeForm()
    ingredients = db.session.execute(db.select(Ingredient).order_by(Ingredient.name)).scalars()
    form.ingredients.choices = [(ingredient.id, ingredient.name) for ingredient in ingredients]
    return render_template('home.html', form=form)

@app.route('/ingredients')
def show_ingredients():
    form = IngredientForm()
    return render_template('ingredients.html', form=form)

@app.route('/api/cupcakes')
def return_cupcakes():
    all_cupcakes = db.session.execute(db.select(Cupcake).order_by(Cupcake.flavor)).scalars()
    serialized_cupcakes = [cupcake.serialize_cupcake() for cupcake in all_cupcakes]

    return jsonify(cupcakes = serialized_cupcakes)

@app.route('/api/cupcakes', methods=["POST"])
def add_cupcake():
    print('******************************************')
    print(request.json)
    print('******************************************')
    flavor = request.json['flavor']
    size = request.json['size']
    rating = request.json['rating']
    image = request.json.get('image')
    new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)
    ingredients = request.json['ingredients']
    for ingredient in ingredients: 
        current_ingredient = db.session.query(Ingredient).filter(Ingredient.id == ingredient).first()
        new_cupcake.ingredients.append(current_ingredient)
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

@app.route('/api/ingredients')
def return_ingredients():
    all_ingredients = db.session.execute(db.select(Ingredient).order_by(Ingredient.name)).scalars()
    serialized_ingredients = [ingredient.serialize_ingredient() for ingredient in all_ingredients]

    return jsonify(ingredients = serialized_ingredients)

@app.route('/api/ingredients', methods=["POST"])
def add_ingredient():
    name = request.json['name']
    new_ingredient = Ingredient(name=name)
    db.session.add(new_ingredient)
    db.session.commit()

    return (jsonify(ingredient = new_ingredient.serialize_ingredient()), 201)

@app.route('/api/ingredients/<int:id>', methods=["PATCH"])
def update_ingredient(id):
    ingredient = Ingredient.query.get_or_404(id)
    ingredient.name = request.json.get('name', ingredient.name)
    db.session.commit()

    return jsonify(ingredient = ingredient.serialize_ingredient())


# 2 add functionality on front end to update a cupcake
    # update form fill
    # api update function (to include ingredients)
    # axios update function
# 1 add testing (flask & javascript)
    # run testing
# 0 remove logging logic