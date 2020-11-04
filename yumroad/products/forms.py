from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import Length, DataRequired


class ProductForm(FlaskForm):
    name = StringField(
        "Name",
        validators=[
            DataRequired(),
            Length(
                min=4,
                max=255,
                message="The product name must be between 4 and 255 characters long.",
            )
        ],
    )
    description = TextAreaField(
        "Description",
        [
            Length(
                max=150,
            )
        ],
    )
