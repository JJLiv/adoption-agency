from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SelectField
from wtforms.validators import InputRequired, Optional, NumberRange, URL


class PetForm(FlaskForm):
    """Form for adding a new pet"""
    name = StringField("Pet Name", validators=[InputRequired(message="Must enter a pets name")])
    species = SelectField("Species", choices=[{'cat','cat'},{'dog','dog'},{'porc','porcupine'}])
    photo_url = StringField("Photo URL", validators=[URL(message="Must be a valid photo URL"),Optional()])
    age = IntegerField("Age", validators=[NumberRange(min=0, max=30, message='Must enter an age between zero and thirty')])
    notes = StringField("Notes")


    
