from flask import Blueprint, url_for, render_template, redirect

from yumroad.extensions import login_manager
from yumroad.users.models import User
from yumroad.users.forms import RegisterForm

users_bp = Blueprint("users", __name__)


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@users_bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(form.name.data, form.email.data, form.password.data)
        user.save_to_db()
        return redirect(url_for("products.index"))
    return render_template("users/register.jinja2", form=form, title="Resgister")
