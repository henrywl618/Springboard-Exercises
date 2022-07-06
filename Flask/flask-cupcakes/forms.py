from flask_wtf import FlaskForm
from wtforms import FloatField,StringField
from wtforms.validators import InputRequired,NumberRange

class CupcakeForm(FlaskForm):
    flavor = StringField('Flavor',validators=[InputRequired()])
    size = StringField('Size',validators=[InputRequired()])
    rating = FloatField('Rating',validators=[InputRequired(),NumberRange(min=0,max=10)])
    image = StringField('Image URL')