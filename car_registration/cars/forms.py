from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import SubmitField, SelectField

class CarForm(FlaskForm):
    color = SelectField('Color', choices=[('yellow', 'yellow'), ('blue', 'blue'), ('gray', 'gray')], validators=[DataRequired()])
    car_type = SelectField('Car Type', choices=[('hatch', 'hatch'), ('sedan', 'sedan'), ('convertible', 'convertible')], validators=[DataRequired()])
    owner_id = SelectField('Owner', choices=[])
    submit = SubmitField("Submit")