from flask import Blueprint, render_template
from yumroad.stores.models import Store

stores_bp = Blueprint("stores", __name__)


@stores_bp.route("/")
def index():
    stores = Store.query.all()
    return render_template("stores/index.html", stores=stores)


@stores_bp.route("<string:store_slug>")
def show(store_slug):
    store = Store.find_by_slug(store_slug)
    if not store:
        abort(404)
    return render_template("stores/show.html", store=store, title=store.name)