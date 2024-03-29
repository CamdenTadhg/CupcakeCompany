"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Cupcake(db.Model):
    """model for cupcakes"""

    __tablename__ = 'cupcakes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.Text, nullable=False, unique=True)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.Text, default='https://tinyurl.com/demo-cupcake')

    ingredients = db.relationship('Ingredient', secondary='recipelines', back_populates='cupcakes')

    def serialize_cupcake(self):
        return {
            "id" : self.id,
            "flavor" : self.flavor,
            "size" : self.size,
            "rating" : self.rating,
            "image" : self.image,
        }
    
    def serialize_ingredients(self):
        ingredients_list = []
        for ingredient in self.ingredients:
            ingredients_list.append(ingredient.id)
        return {
            "ingredients": ingredients_list
        }
    
class Ingredient(db.Model):
    """model for ingredients"""

    __tablename__ = 'ingredients'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False, unique=True)

    def serialize_ingredient(self):
        return {
            "id" : self.id,
            "name" : self.name
        }
    
    cupcakes = db.relationship('Cupcake', secondary='recipelines', back_populates='ingredients')

class RecipeLine(db.Model):
    """recipe lines for many to many relationship between cupcakes and ingredients"""

    __tablename__ = "recipelines"

    cupcake_id = db.Column(db.Integer, db.ForeignKey('cupcakes.id'), primary_key=True)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredients.id'), primary_key=True)