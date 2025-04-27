from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SubmitField, PasswordField
class TaskForm(FlaskForm):
    title = StringField('Title')
    description = TextAreaField('Description')
    completed = BooleanField('Completed')
    submit = SubmitField('Submit')
    
class UserForm(FlaskForm):
    username = StringField('Username')
    first_name = StringField('firstname')
    last_name = StringField('lastname')
    password = PasswordField('Password')
    submit = SubmitField('Submit')
    
# class LoginForm(FlaskForm):
#     username = StringField('Username')
#     password = StringField('Password')
#     submit = SubmitField('Login')
# class RegistrationForm(FlaskForm):
#     username = StringField('Username')
#     email = StringField('Email')
#     password = StringField('Password')
#     submit = SubmitField('Register')
    