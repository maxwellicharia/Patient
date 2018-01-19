from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators, SubmitField


class Form(FlaskForm):

    id = IntegerField('Id: ', [validators.DataRequired(message="Required field")])
    name = StringField('Name: ',  [validators.DataRequired(message="Required field")])
    age = IntegerField('Age: ', [validators.DataRequired(message="Required field")])
    submit = SubmitField("Submit")

