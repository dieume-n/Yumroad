from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, BooleanField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

from yumroad.users.models import User
from yumroad.stores.models import Store


class RegisterForm(FlaskForm):
    store = StringField("Store name", validators=[DataRequired(), Length(min=4)])
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

    def validate_store(self, store):
        store = Store.find_by_slug(store.data)
        if store:
            raise ValidationError(f"A store with the name {store.data} already exist")
        return True


class LoginForm(FlaskForm):
    email = EmailField(
        "Email address",
        validators=[DataRequired(), Email("Please provide a valid email address")],
    )
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember me")
