from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import Required, Email, EqualTo, Length, ValidationError

from yumroad.users.models import User


class RegisterForm(FlaskForm):
    name = StringField("Name")
    email = EmailField("Email address", validators=[Email(), Required()])
    password = PasswordField(
        "Password",
        validators=[
            Required(),
            Length(min=5),
            EqualTo("confirm", message="Passwords must match"),
        ],
    )
    confirm = PasswordField("Confirm password", validators=[Required()])

    def validate_email(self, email):
        user = User.find_by_email(email)
        if not user:
            raise ValidationError("This email is already taken")
        return True
