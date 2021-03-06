from sqlalchemy.orm import validates

from yumroad.extensions import db
from yumroad.model import BaseModel
from yumroad.stores.models import Store


class Product(BaseModel):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(150), nullable=True)
    store_id = db.Column(db.Integer, db.ForeignKey(Store.id), nullable=False)
    price_cents = db.Column(db.Integer)
    picture_url = db.Column(db.String, default="default.png")

    store = db.relationship("Store", uselist=False, back_populates="products")

    @validates("name")
    def validate_name(self, key, name):
        if len(name.strip()) <= 3:
            raise ValueError(
                "The name of the product must be greater than 3 characters long"
            )
        return name

    @property
    def picture(self):
        return f"img/{self.picture_url}"
