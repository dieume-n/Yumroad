from yumroad.models import BaseModel
from yumroad.extensions import db


class Store:
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    products = db.relationship("Product", back_populates="store")
    owner = db.relationship("User", uselist=False, back_populates="store")

    @validates("name")
    def validate_name(self, key, name):
        if len(name.strip()) <= 3:
            raise ValueError("The store name must be greater than 3 characters long")
        return name
