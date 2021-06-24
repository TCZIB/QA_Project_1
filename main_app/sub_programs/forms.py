from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DateField, SubmitField
from wtforms.validators import Length, DataRequired, ValidationError
from wtforms.widgets import TextArea
from sub_programs.models import Movies, MovieReviews, ReviewLikes, Users

profanities = ["Shit", "Fuck"]
  
class Movie_Review_Form(FlaskForm):
    username = StringField("Your name: ", validators=[DataRequired(), Length(min=5, max=30)])
    review = StringField("Your review: ", widget=TextArea(),validators=[DataRequired(), Length(min=1, max=500)])
    submit = SubmitField("Submit")

    def validate_review_contents(self, review):
        if profanities in review.lower():
            raise ValidationError("Please make sure content is clean!")

class Login_Form(FlaskForm):
    form_username = StringField("Your Username: ", validators=[DataRequired(), Length(min=1, max=30)])
    form_password = StringField("Your Password: ", validators=[DataRequired(), Length(min=1, max=30)])
    submit = SubmitField("Login")

class Modify_Confirm(FlaskForm):
    submit = SubmitField("Delete")
    cancel = SubmitField("Cancel")
    modify = SubmitField("Update")
    add = SubmitField("Add")
    
    movie_title = StringField("Movie title")
    movie_age = StringField("Movie title")
    movie_description = StringField("Movie title", widget=TextArea())
    movie_runtime = StringField("Movie title")
    movie_cover_art = StringField("Movie title")


