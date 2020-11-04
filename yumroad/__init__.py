from flask import Flask, render_template

from yumroad.config import configurations
from yumroad.extensions import db, migrate, csrf, bcrypt, login_manager


from yumroad.products.views import products_bp
from yumroad.users.views import users_bp
from yumroad.products.commands import products_cli


def page_not_found(e):
    return render_template("errors/404.html"), 404


def create_app(environment_name="dev"):

    app = Flask(__name__)
    app.config.from_object(configurations[environment_name])

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    # Register Blueprints
    app.register_blueprint(products_bp, url_prefix="/products")
    app.register_blueprint(users_bp)

    # Register Commads
    app.cli.add_command(products_cli)

    # Error pages
    app.register_error_handler(404, page_not_found)

    return app