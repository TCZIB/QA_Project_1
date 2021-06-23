from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DateField, SubmitField
from wtforms.validators import Length, DataRequired, ValidationError
from wtforms.widgets import TextArea

profanities = ["Shit", "Fuck"]

class Movie_Review_Form(FlaskForm):
    username = StringField("Your name: ", validators=[DataRequired(), Length(min=5, max=30)])
    review = StringField("Your review: ", widget=TextArea(),validators=[DataRequired(), Length(min=1, max=500)])
    submit = SubmitField("Submit")

    def validate_review_contents(self, review):
        if profanities in review.lower():
            raise ValidationError("Please make sure content is clean!")

