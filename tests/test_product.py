import pytest
from flask import url_for

from yumroad.extensions import db
from yumroad.products.models import Product


@pytest.fixture
def sample_book():
    book = Product(name="Sherlock Holmes", description="A house hunting detective")
    book.save_to_db()
    return book


def test_product_creation(client, init_database):
    assert Product.query.count() == 0
    book = Product(name="Sherlock Holmes", description="A house hunting detective")
    book.save_to_db()
    assert Product.query.count() == 1
    assert Product.query.first().name == book.name


def test_name_validation(client, init_database):
    with pytest.raises(ValueError):
        Product(name="  a", description="inivalid product")