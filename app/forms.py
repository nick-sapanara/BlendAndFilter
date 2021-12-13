from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectMultipleField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Next')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


class RegistrationForm2(FlaskForm):
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Next')


class RegistrationForm3(FlaskForm):
    tag = SelectMultipleField('What Kind of Coffee Do You Enjoy?', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Create Account!')


class AddShopForm(FlaskForm):
    shopName = StringField('Shop', validators=[DataRequired()])
    ownerName = StringField('Owner', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    website = StringField('Website', validators=[DataRequired()])
    submit = SubmitField('Submit')


class AddShopForm2(FlaskForm):
    about_me = TextAreaField('About Shop', validators=[Length(min=0, max=140)])
    submit = SubmitField('Next')


class RegistrationForm3(FlaskForm):
    tag = SelectMultipleField("What's Your Favorite Coffee?", coerce=int, validators=[DataRequired()])
    submit = SubmitField('Create Account!')


class SearchForm(FlaskForm):
    city = TextAreaField('city', validators=[Length(min=0)])
    state = SelectField('State', choices=["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"], coerce=str)
    submit = SubmitField('Blend!')