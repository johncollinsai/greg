''' A webform, web form or HTML form on a web page allows a user to enter data.
I use flask-wtf extension. flask-wtf uses python classes to represent web
forms (i.e., each form is a class) and a form class simply defines the fields 
of the form as class variables. This module, forms.py, therefore stores my
web form classes.
'''

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, \
    TestAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, \
    Length
from app.models import Post

''' NB: MUST INCLUDE IN EVERY FORM the form.hidden_tag() template argument.
{{ form.hidden_tag() }} generates a hidden field that includes a token that is 
used to protect the form against CSRF attacks. All I need to do to have the form 
protected is include this hidden field and have the SECRET_KEY variable defined 
in config.py. If I take care of these two things, Flask-WTF does the rest.
'''

# A basic post form may be helpful?
class PostForm(FlaskForm):
    post = TextAreaField('Say something', validators=[DataRequired()])
    submit = SubmitField('Submit')


