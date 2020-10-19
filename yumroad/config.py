import os


class BaseConfig:
    TESTING = False
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "mysql://root:pwd@localhost:3306"


class DevConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:/// dev.db"
    SQLALCHEMY_ECHO = True


class TestConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:/// test.db"


class ProdConfig(BaseConfig):
    pass


configurations = {"dev": DevConfig, "test": TestConfig, "prod": ProdConfig}
