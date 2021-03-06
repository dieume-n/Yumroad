from flask import Flask, render_template

from yumroad.config import configurations
from yumroad.extensions import db, migrate, csrf, bcrypt, login_manager, assets

from yumroad.users.views import users_bp
from yumroad.stores.views import stores_bp
from yumroad.products.views import products_bp
from yumroad.products.commands import products_cli


def page_not_found(e):
    return render_template("errors/404.html"), 404


def create_app(environment_name="dev"):
    app = Flask(__name__)
    app.config.from_object(configurations[environment_name])

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)
    csrf.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    assets.init_app(app)

    # Register Blueprints
    app.register_blueprint(stores_bp, url_prefix="/stores")
    app.register_blueprint(users_bp)
    app.register_blueprint(products_bp, url_prefix="/products")

    # Register Commads
    app.cli.add_command(products_cli)

    # Error pages
    app.register_error_handler(404, page_not_found)

    @app.route("/")
    def index():
        return render_template("layoutv2.html")

    return app
