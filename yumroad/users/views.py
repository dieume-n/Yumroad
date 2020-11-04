from flask import Blueprint, url_for, render_template, redirect, flash
from flask_login import current_user, login_user, logout_user, login_required

from yumroad.extensions import login_manager
from yumroad.users.models import User
from yumroad.users.forms import RegisterForm, LoginForm

users_bp = Blueprint("users", __name__)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@users_bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(form.name.data, form.email.data, form.password.data)
        user.save_to_db()
        return redirect(url_for("products.index"))
    return render_template("users/register.html", form=form, title="Resgister")


@users_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("products.index"))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.find_by_email(form.email.data)

        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for("products.index"))
        else:
            flash("Invalid email or password", category="danger")
    return render_template("users/login.html", form=form, title="Login")


@login_required
@users_bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("products.index"))
