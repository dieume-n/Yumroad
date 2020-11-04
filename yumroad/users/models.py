from flask_login import UserMixin

from yumroad.extensions import db, bcrypt
from yumroad.model import BaseModel


class User(BaseModel, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    password = db.Column(db.String(255))

    def __init__(self, name, email, password):
        self.name = name.title()
        self.email = email.lower().strip()
        self.password = bcrypt.generate_password_hash(password)

    @classmethod
    def find_by_email(cls, email):
        user = cls.query.filter_by(email=email).first()
        if not user:
            return False
        return user

    def check_password(self, password):
        if not bcrypt.check_password_hash(self.password, password):
            return False
        return True
