from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    
    pitch = TextAreaField(' Your Pitch', validators = [Required()])
    category = SelectField('Pitch Category', choices=[('Inspirational','Inspirational'),('Biography','Biography'),('Business','Business'),('Ideas','Ideas')])
    submit = SubmitField('Submit')