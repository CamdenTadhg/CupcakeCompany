from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, URL, NumberRange, AnyOf

class AddCupcakeForm(FlaskForm):
    """form for adding a cupcake to the database"""

    flavor = StringField("Flavor", validators=[InputRequired(message="Please enter a flavor")])
    size = StringField("Size", validators=[InputRequired(message="Please enter a size"), AnyOf(values=["extra small", "small", "medium", "large", "extra large"], message="Please enter a valid size")])
    rating = IntegerField("Rating", validators=[NumberRange(min=1, max=10, message="Please enter a number between 1 and 10")])
    image = StringField("Photo URL", validators=[URL(message="Please enter a valid URL")])

class UpdateCupcakeForm(FlaskForm):
    """form for updating a cupcake in the database"""

    size = StringField("Size", validators=[InputRequired(message="Please enter a size"), AnyOf(values=["extra small", "small", "medium", "large", "extra large"], message="Please enter a valid size")])
    rating = IntegerField("Rating", validators=[NumberRange(min=1, max=10, message="Please enter a number between 1 and 10")])

class IngredientForm(FlaskForm):
    """form for adding and updating ingredients in the database"""

    name = StringField("Ingredient Name", validators=[InputRequired(message="Please enter an ingredient")])
