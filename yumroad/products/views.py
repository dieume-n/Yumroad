import click
from flask import Blueprint, render_template
from yumroad.products.models import Product

products_bp = Blueprint("products", __name__)


@products_bp.route("/")
def index():
    products = Product.query.all()
    return render_template("products/index.html", products=products)


@products_bp.route("<int:product_id>")
def details(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template("products/details.html", product=product)