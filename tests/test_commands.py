import pytest
import click
from yumroad.products.models import Product
from yumroad.products.commands import seed


def test_seed_products_command(app, client, init_database):
    runner = app.test_cli_runner()
    result = runner.invoke(seed, ["5"])

    assert result.exit_code == 0
    assert Product.query.count() == 5
