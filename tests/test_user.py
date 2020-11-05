import pytest
from flask import url_for
from yumroad.users.models import User

EXAMPLE_NAME = "John Smith"
EXAMPLE_EMAIL = "john@example.com"
EXAMPLE_PASSWORD = "testing101"

VALID_REGISTER_PARAMS = {
    "name": EXAMPLE_NAME,
    "email": EXAMPLE_EMAIL,
    "password": EXAMPLE_PASSWORD,
    "confirm": EXAMPLE_PASSWORD,
}


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


def test_get_register(client, init_database):
    response = client.get(url_for("users.register"))

    assert response.status_code == 200
    assert b"Register" in response.data
    assert b"Already have an account?" in response.data


def test_post_register(client, init_database):
    response = client.post(
        url_for("users.register"), data=VALID_REGISTER_PARAMS, follow_redirects=True
    )
    user = User.query.filter_by(email=VALID_REGISTER_PARAMS["email"]).first()
    assert response.status_code == 200
    assert user.name == VALID_REGISTER_PARAMS["name"]
    assert user.email == VALID_REGISTER_PARAMS["email"]
    assert user.password != VALID_REGISTER_PARAMS["password"]
