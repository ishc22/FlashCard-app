from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField, EmailField, TextAreaField
from wtforms.validators import InputRequired, EqualTo

class SignupForm(FlaskForm):
    email = EmailField('Email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[InputRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Log In')

class CreateDeckForm(FlaskForm):
    deck_name = StringField('Name Of The Deck', validators=[InputRequired()])
    submit = SubmitField('Create')

class CreateCardForm(FlaskForm):
    question = StringField('Question', validators=[InputRequired()])
    answer = TextAreaField('Answer', validators=[InputRequired()])
    submit = SubmitField('Create')

