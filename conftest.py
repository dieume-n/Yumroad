import pytest

from yumroad import create_app
from yumroad.extensions import db
from yumroad.users.models import User


@pytest.fixture
def app():
    return create_app("test")


@pytest.fixture
def init_database():
    db.create_all()
    yield
    db.drop_all()


@pytest.fixture
def authenticated_request(client):
    user = User("john Doe", "john@doe.com", "secret")
    user.save_to_db()

    response = client.post(
        url_for("users.login"),
        data=dict(email=user.email, password="secret"),
        follow_redirects=True,
    )
    yield client
