"""first migration

Revision ID: 5d6dd67c128b
Revises: 93630e3be2f6
Create Date: 2023-02-26 19:33:40.321116

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d6dd67c128b'
down_revision = '93630e3be2f6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('portfolio',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('symbol', sa.String(length=16), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('shares', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('cash', sa.Float(precision=16), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('transactions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('stock_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('transaction_time', sa.DateTime(timezone=64), nullable=True),
    sa.Column('price', sa.Float(precision=32), nullable=True),
    sa.Column('total', sa.Float(precision=16), nullable=True),
    sa.ForeignKeyConstraint(['stock_id'], ['portfolio.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transactions')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_table('user')
    op.drop_table('portfolio')
    # ### end Alembic commands ###
