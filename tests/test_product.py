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

    expected_link = url_for("products.show", product_id=sample_book.id)
    assert expected_link in str(response.data)


def test_products_show_page(client, init_database, sample_book):
    response = client.get(url_for("products.show", product_id=sample_book.id))
    assert response.status_code == 200
    assert "Yumroad" in str(response.data)


def test_not_found(client, init_database):
    response = client.get(url_for("products.show", product_id=1))
    assert response.status_code == 404
    assert url_for("products.index") in str(response.data)


def test_create_page(client, init_database):
    response = client.get(url_for("products.create"))

    assert response.status_code == 200
    assert b"Name" in response.data
    assert b"Create" in response.data


def test_create_product(client, init_database):
    response = client.post(
        url_for("products.create"),
        data=dict(name="test product", description="is persisted"),
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert Product.query.count() == 1
    assert Product.query.first().name == "test product"
    assert b"test product" in response.data
    assert b"Purchase" in response.data


def test_invalid_create_product(client, init_database):
    response = client.post(
        url_for("products.create"),
        data=dict(name="abc", description="invalid product"),
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert (
        b"The product name must be between 4 and 255 characters long" in response.data
    )


def test_edit_product_page(client, init_database, sample_book):
    response = client.get(url_for("products.edit", product_id=sample_book.id))

    assert response.status_code == 200
    assert sample_book.name in str(response.data)
    assert sample_book.description in str(response.data)
    assert b"Edit" in response.data


def test_edit_product_submission(client, init_database, sample_book):
    old_name = sample_book.name
    old_description = sample_book.description
    response = client.post(
        url_for("products.edit", product_id=sample_book.id),
        data=dict(name="test-change", description="is persisted"),
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert "test-change" in str(response.data)
    assert "is persisted" in str(response.data)
    assert old_name not in str(response.data)
    assert old_description not in str(response.data)
    assert b"Edit" in response.data
