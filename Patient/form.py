from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators, SubmitField

class Form(FlaskForm):

    name = StringField('Name: ',  [validators.DataRequired(message="Required field")])
    submit = SubmitField("Submit")

