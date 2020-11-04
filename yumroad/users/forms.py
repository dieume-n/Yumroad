from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

from yumroad.users.models import User


class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = EmailField(
        "Email address",
        validators=[Email("Please provide a valid email address"), DataRequired()],
    )
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Length(min=5),
            EqualTo("confirm", message="Passwords must match"),
        ],
    )
    confirm = PasswordField("Confirm password", validators=[DataRequired()])

    def validate_email(self, email):
        user = User.find_by_email(email.data)

        if user:
            raise ValidationError("This email is already taken")
        return True
