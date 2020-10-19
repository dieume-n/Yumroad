from sqlalchemy.orm import validates

from yumroad.extensions import db
from yumroad.model import BaseModel


class Product(BaseModel):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(150), nullable=True)

    @validates("name")
    def validate_name(self, key, name):
        if len(name.strip()) <= 3:
            raise ValueError(
                "The name of the product must be greater than 3 characters long"
            )
        return name
