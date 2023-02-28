from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, ValidationError


class newUser(FlaskForm):
    label = StringField('Ajouter utilisateur', validators=[DataRequired()])
