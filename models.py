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

    recipelines = db.relationship('RecipeLine', backref='cupcakes')

    def serialize_cupcake(self):
        return {
            "id" : self.id,
            "flavor" : self.flavor,
            "size" : self.size,
            "rating" : self.rating,
            "image" : self.image
        }
    
class Ingredient(db.Model):
    """model for ingredients"""

    __tablename__ = 'ingredients'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False, unique=True)

    cupcakes = db.relationship('Cupcake', secondary='recipelines', backref='ingredients')
    recipelines = db.relationship('RecipeLine', backref='ingredients')

    def serialize_ingredient(self):
        return {
            "id" : self.id,
            "name" : self.name
        }

class RecipeLine(db.Model):
    """recipe lines for many to many relationship between cupcakes and ingredients"""

    __tablename__ = "recipelines"

    cupcake_id = db.Column(db.Integer, db.ForeignKey('cupcakes.id'), primary_key=True)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredients.id'), primary_key=True)

    def serialize_recipeline(self):
        return {
            "cupcake_id" : self.cupcake_id, 
            "ingredient_id" : self.ingredient_id,
        }