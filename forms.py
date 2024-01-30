from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import DataRequired, ValidationError, Optional, URL, NumberRange

class AddPetForm(FlaskForm):
    def validate_species(form, field):
        if field.data.lower() not in ('cat', 'dog', 'porcupine'):
            raise ValidationError('Species must be either cat, dog, or porcupine')

    name = StringField('Name', validators=[DataRequired(message='Name is required.')])
    species = StringField('Species', validators=[DataRequired(message='Species is required'), validate_species])
    photo_url = StringField('Photo URL', validators=[Optional(), URL(message='Must be a URL')])
    age = IntegerField('Age', validators=[Optional(), NumberRange(min=0, max=30, message='Age must be between 0 and 30.')])
    notes = StringField('Notes')

class EditPetForm(FlaskForm):
    photo_url = StringField('Photo URL', validators=[Optional(), URL(message='Must be a URL')])
    notes = StringField('Notes')
    available = BooleanField('Available')