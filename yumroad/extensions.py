from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from faker import Faker

db = SQLAlchemy()
migrate = Migrate()
fake = Faker("en_US")
