from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, URLField, BooleanField, FileField
from wtforms.validators import InputRequired,Optional,NumberRange,AnyOf

class PetForm(FlaskForm):
    """Form for adding pets"""
    name = StringField('Name',validators=[InputRequired(message='Name is required.')])
    species = StringField('Species',validators=[InputRequired(message='Species is required.'), AnyOf(['cat','dog','porcupine','Cat','Dog','Porcupine'],message="Species can only be a dog, cat or porcupine.")])
    photo_url = URLField('Photo Link',validators=[Optional()])
    photo_file = FileField('Upload Image',validators=[Optional()])
    age = IntegerField ('Age',validators=[NumberRange(min=0,max=30,message='Age must be between 0 and 30')])
    notes = StringField('Notes')
    available = BooleanField('Available')

class PetEditForm(FlaskForm):
    """Form for editing existing pets"""
    photo_url = StringField('Photo Link',validators=[Optional()])
    notes = StringField('Notes')
    available = BooleanField('Available')