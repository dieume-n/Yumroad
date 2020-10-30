from flask import Flask, render_template

from yumroad.config import configurations
from yumroad.extensions import db, migrate


from yumroad.products.views import products_bp
from yumroad.products.commands import products_cli


def page_not_found(e):
    return render_template("errors/404.jinja2"), 404


def server_error(e):
    return render_template("errors/500.jinja2"), 500


def create_app(environment_name="dev"):

    app = Flask(__name__)
    app.config.from_object(configurations[environment_name])

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints
    app.register_blueprint(products_bp, url_prefix="/products")

    # Register Commads
    app.cli.add_command(products_cli)

    # Error pages
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(500, server_error)

    return app