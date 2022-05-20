from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, DateTimeField
from wtforms.validators import DataRequired, url

class CafeForm(FlaskForm):
    cafeName = StringField(label='Cafe Name', validators=[DataRequired('Field cannot be blank')])
    location = StringField(label='Location', validators=[DataRequired('Field cannot be blank'), url('web address required')])
