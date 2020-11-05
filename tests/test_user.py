import pytest
from flask import url_for
from yumroad.users.models import User

EXAMPLE_NAME = "John Smith"
EXAMPLE_EMAIL = "john@example.com"
EXAMPLE_PASSWORD = "testing101"


def create_user(name=EXAMPLE_NAME, email=EXAMPLE_EMAIL, password=EXAMPLE_PASSWORD):
    user = User(name=name, email=email, password=password)
    user.save_to_db()
    return user


def test_user_creation(client, init_database):
    assert User.query.count() == 0
    user = create_user()
    assert User.query.count() == 1
    assert user.name == EXAMPLE_NAME
    assert user.email == EXAMPLE_EMAIL
    assert user.password is not EXAMPLE_PASSWORD