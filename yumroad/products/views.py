import click
from sqlalchemy import desc
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from yumroad.products.models import Product
from yumroad.products.forms import ProductForm

products_bp = Blueprint("products", __name__)


@products_bp.route("/")
def index():
    products = Product.query.order_by(desc(Product.updated)).all()
    return render_template(
        "products/index.html", products=products, title="All Products"
    )


@products_bp.route("<int:product_id>")
def show(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template("products/show.html", product=product, title=product.name)


@products_bp.route("create", methods=["GET", "POST"])
def create():
    form = ProductForm()

    if form.validate_on_submit():
        product = Product(name=form.name.data, description=form.description.data)
        product.save_to_db()
        return redirect(url_for("products.show", product_id=product.id))
    return render_template("products/create.html", title="Create Product", form=form)


@products_bp.route("<int:product_id>/edit", methods=["GET", "POST"])
def edit(product_id):
    product = Product.query.get_or_404(product_id)
    form = ProductForm(obj=product)

    if form.validate_on_submit():
        product.name = form.name.data
        product.description = form.description.data
        product.save_to_db()
        return redirect(url_for("products.show", product_id=product_id))
    return render_template(
        "products/edit.html", form=form, product=product, title=product.name
    )
