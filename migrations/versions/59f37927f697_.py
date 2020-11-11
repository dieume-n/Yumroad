"""empty message

Revision ID: 59f37927f697
Revises: 0e29f34b00fd
Create Date: 2020-11-11 12:18:19.792759

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59f37927f697'
down_revision = '0e29f34b00fd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('stores', schema=None) as batch_op:
        batch_op.add_column(sa.Column('slug', sa.String(length=255), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('stores', schema=None) as batch_op:
        batch_op.drop_column('slug')

    # ### end Alembic commands ###
