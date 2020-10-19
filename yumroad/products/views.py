from flask import Blueprint
from yumroad.products.models import Product


products_bp = Blueprint("products", __name__)


@products_bp.route("/")
def index():
    return "All of the products"


@products_bp.route("<int:product_id>")
def details(product_id):
    pass