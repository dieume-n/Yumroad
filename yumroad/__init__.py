from flask import Flask

from yumroad.config import configurations
from yumroad.extensions import db, migrate


def create_app(environment_name="dev"):

    app = Flask(__name__)
    app.config.from_object(configurations[environment_name])

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    return app