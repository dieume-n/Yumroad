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


def test_products_index_page(client, init_database, sample_book):
    response = client.get(url_for("products.index"))
    assert response.status_code == 200
    assert "Yumroad" in str(response.data)
    assert sample_book.name in str(response.data)

    expected_link = url_for("products.details", product_id=sample_book.id)
    assert expected_link in str(response.data)
