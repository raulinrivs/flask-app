from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField

class OwnerForm(FlaskForm):
    name = StringField("Name: ", validators=[DataRequired()])
    submit = SubmitField("Submit")