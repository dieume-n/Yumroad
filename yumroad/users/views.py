from flask import Blueprint


from yumroad.users.models import User

users_bp = Blueprint("users", __name__)
