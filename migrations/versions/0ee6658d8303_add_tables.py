"""add tables

Revision ID: 0ee6658d8303
Revises: 1ddd7f56e894
Create Date: 2023-04-25 11:42:59.834475

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ee6658d8303'
down_revision = '1ddd7f56e894'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('deck', schema=None) as batch_op:
        batch_op.add_column(sa.Column('deck_name', sa.String(length=100), nullable=False))
        batch_op.drop_column('name')

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=1000),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=1000),
               nullable=True)

    with op.batch_alter_table('deck', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.VARCHAR(length=100), nullable=False))
        batch_op.drop_column('deck_name')

    # ### end Alembic commands ###