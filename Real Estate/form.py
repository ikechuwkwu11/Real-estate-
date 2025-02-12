from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,IntegerField
from wtforms.validators import DataRequired

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    access_code = StringField('Access_Code', validators=[DataRequired()])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class PropertyForm(FlaskForm):
    title = SubmitField('Title', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])


