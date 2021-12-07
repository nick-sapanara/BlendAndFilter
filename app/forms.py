from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectMultipleField
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
    about_shop = TextAreaField('About Shop', validators=[Length(min=0, max=140)])
    submit = SubmitField('Create Shop')

