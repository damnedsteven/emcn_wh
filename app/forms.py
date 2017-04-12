# from flask_wtf import Form
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, Length, InputRequired, Email

from app.models import User

class LoginForm(FlaskForm):
    # openid = StringField('openid', validators=[DataRequired()])
    username = StringField('username', validators=[InputRequired(), Length(min=1, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember_me = BooleanField('remember_me', default=False)
	
class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=120)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])

class EditForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    about_me = TextAreaField('about_me', validators=[Length(min=0, max=140)])
	
    def __init__(self, original_username, *args, **kwargs):
        FlaskForm.__init__(self, *args, **kwargs)
        self.original_username = original_username

    def validate(self):
        if not FlaskForm.validate(self):
            return False
        if self.username.data == self.original_username:
            return True
        user = User.query.filter_by(username=self.username.data).first()
        if user != None:
            self.username.errors.append('This username is already in use. Please choose another one.')
            return False
        return True
		
class PostForm(FlaskForm):
    post = StringField('post', validators=[DataRequired()])
	
class SearchForm(FlaskForm):
    search = StringField('search', validators=[DataRequired()])