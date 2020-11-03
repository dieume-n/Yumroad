import click
from flask.cli import AppGroup
from yumroad.extensions import fake

from yumroad.products.models import Product


products_cli = AppGroup("products")


@products_cli.command("seed")
@click.argument("count")
def seed(count=10):
    """ Seed products """
    print(f"Seeding {count} products")
    for i in range(int(count)):
        product = Product(name=f"Product{i}", description=fake.text()[:150])
        product.save_to_db()

    print(f"{count} products seeded")
