from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FileField, StringField, SubmitField, SelectField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import Required, Email, Length, EqualTo
from ..models import User
from wtforms import ValidationError

class PostForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    category = SelectField('Pitch Category', choices=[('Sales','Sales'),('Interview','Interview'),
    ('Elevator','Elevator'),('Promotion','Promotion'),('Personal','Personal'),
    ('Pickup-lines','Pickup-lines')],validators=[Required()])
    post = TextAreaField('Pitch', validators=[Required()])
    submit = SubmitField('Post Pitch')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class CatForm(FlaskForm):
    name = StringField('Category Name', validators=[Required(), Length(1, 64)])
    submit = SubmitField('Submit')

