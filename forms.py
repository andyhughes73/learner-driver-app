from flask_wtf import FlaskForm
from peewee import CharField
from wtforms import StringField, PasswordField, TextAreaField
from wtforms import validators
from wtforms.validators import (DataRequired, Regexp, ValidationError, Email,
                               Length, EqualTo)

from models import User


def name_exists(form, field):
    if User.select().where(User.username == field.data).exists():
        raise ValidationError('User with that name already exists.')


def email_exists(form, field):
    if User.select().where(User.email == field.data).exists():
        raise ValidationError('User with that email already exists.')


class RegisterForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[
            DataRequired(),
            Regexp(
                r'^[a-zA-Z0-9_]+$',
                message=("Username should be one word, letters, "
                         "numbers, and underscores only.")
            ),
            name_exists
        ])
    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email(),
            email_exists
        ])
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=2),
            EqualTo('password2', message='Passwords must match')
        ])
    password2 = PasswordField(
        'Confirm Password',
        validators=[DataRequired()]
    )
    

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])


class PostForm(FlaskForm):
    content = TextAreaField("What's up?", validators=[DataRequired()])


class StandardForm(FlaskForm):
    section = TextAreaField('Set section title', validators=[DataRequired()])
    standard = TextAreaField('Enter the standard to be added', validators=[DataRequired()])

    
class FaultForm(FlaskForm):
    section = TextAreaField('Set section title', validators=[DataRequired()])
    fault = TextAreaField('Enter fault', validators=[DataRequired()])