from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_wtf.csrf import CSRFProtect

from faker import Faker

db = SQLAlchemy()
migrate = Migrate()
fake = Faker("en_US")
csrf = CSRFProtect()
bcrypt = Bcrypt()
