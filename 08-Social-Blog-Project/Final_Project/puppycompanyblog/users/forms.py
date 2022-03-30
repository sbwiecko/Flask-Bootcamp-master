from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed # update iamge files

# User Based Imports
from flask_login import current_user
from puppycompanyblog.models import User


class LoginForm(FlaskForm):
    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email()
        ]
    )
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('UserName', validators=[DataRequired()])
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            EqualTo(
                'pass_confirm',
                message='Passwords must match!'
            )
        ]
    )
    pass_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register!')

    # def check_email(self, field):
    #     if User.query.filter_by(email=field.data).first():
    #         raise ValidationError('Your email has been registered already!')

    # def check_username(self, field):
    #     if User.query.filter_by(username=field.data).first():
    #         raise ValidationError('Your username has been registered already!')

    def validate_email(self, field):
        # Check if not None for that user email!
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered already!')

    def validate_username(self, field):
        # Check if not None for that username!
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Sorry, that username is taken!')


class UpdateUserForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('UserName', validators=[DataRequired()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')

    # the prefix `validate_columename` is how the form checks for columns that require validation,
    # just follow the syntax of that function name and write your logic within the function.
    
    # def check_email(self,field):
    #     if User.query.filter_by(email=field.data).first():
    #         raise ValidationError('Your email has been registered already!')

    # def check_username(self,field):
    #     if User.query.filter_by(username=field.data).first():
    #         raise ValidationError('Your username has been registered already!')

    # the profile picture only update when both of username and email are updated to the new one.
    # The problem because the validate_username() and validate_email() function in forms.py
    # that prevent we update data without change both of email and username to the other
    # (that not existing in database).
    # def validate_email(self, field):
    #     # Check if not None for that user email!
    #     if User.query.filter_by(email=field.data).first():
    #         raise ValidationError('Your email has been registered already!')

    # def validate_username(self, field):
    #     # Check if not None for that username!
    #     if User.query.filter_by(username=field.data).first():
    #         raise ValidationError('Sorry, that username is taken!')
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user and user != current_user:
            raise ValidationError('A user with that email already exists.')
 
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user and user != current_user:
            raise ValidationError('This username is taken.')
