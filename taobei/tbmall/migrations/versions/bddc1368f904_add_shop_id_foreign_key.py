"""add shop_id foreign key

Revision ID: bddc1368f904
Revises: dff7d786fe20
Create Date: 2018-11-22 16:50:05.779756

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bddc1368f904'
down_revision = 'dff7d786fe20'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'product', 'shop', ['shop_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'product', type_='foreignkey')
    # ### end Alembic commands ###
