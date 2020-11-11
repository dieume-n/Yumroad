from slugify import slugify
from sqlalchemy import event
from sqlalchemy.orm import validates

from yumroad.model import BaseModel
from yumroad.extensions import db

from yumroad.users.models import User


class Store(BaseModel):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)

    products = db.relationship("Product", back_populates="store")
    owner = db.relationship("User", uselist=False, back_populates="store")

    @validates("name")
    def validate_name(self, key, name):
        if len(name.strip()) <= 3:
            raise ValueError("The store name must be greater than 3 characters long")
        return name

    @staticmethod
    def generate_slug(target, value, old_value, initiator):
        if value and (not target.slug or value != oldvalue):
            target.slug = slugify(value)


event.listen(Store.name, "set", Store.generate_slug, retval=False)
