import os


class BaseConfig:
    TESTING = False
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "mysql://root:pwd@localhost:3306"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", "mysupersecret")
    WTF_CSRF_ENABLED = True


class DevConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///dev.db"
    SQLALCHEMY_ECHO = True


class TestConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
    WTF_CSRF_ENABLED = False


class ProdConfig(BaseConfig):
    SECRET_KEY = os.getenv("SECRET_KEY")


configurations = {"dev": DevConfig, "test": TestConfig, "prod": ProdConfig}
