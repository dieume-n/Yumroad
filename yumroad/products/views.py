import click
from flask import Blueprint, render_template
from yumroad.products.models import Product

products_bp = Blueprint("products", __name__)


@products_bp.route("/")
def index():
    products = Product.query.all()
    return render_template(
        "products/index.jinja2", products=products, title="All Products"
    )


@products_bp.route("<int:product_id>")
def details(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template("products/details.jinja2", product=product)


@products_bp.route("create")
def create():
    return render_template("products/create.jinja2", title="Create Product")
