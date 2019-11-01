"""created the database afresh

Revision ID: f7c7787d5b1a
Revises: 
Create Date: 2019-10-29 15:01:21.189773

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f7c7787d5b1a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('supplier',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=True),
    sa.Column('type', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=90), nullable=False),
    sa.Column('contact', sa.String(length=20), nullable=False),
    sa.Column('address', sa.Text(), nullable=False),
    sa.Column('nationality', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=80), nullable=False),
    sa.Column('contact', sa.String(length=20), nullable=False),
    sa.Column('location', sa.String(length=40), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('contact'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('password'),
    sa.UniqueConstraint('username')
    )
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category', sa.String(length=255), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('comm_type', sa.String(length=255), nullable=False),
    sa.Column('cost_price', sa.Text(), nullable=False),
    sa.Column('markup', sa.Text(), nullable=False),
    sa.Column('discount', sa.Text(), nullable=False),
    sa.Column('selling_price', sa.Text(), nullable=False),
    sa.Column('stock', sa.Text(), nullable=False),
    sa.Column('unit', sa.Text(), nullable=True),
    sa.Column('tax', sa.String(length=255), nullable=False),
    sa.Column('code1', sa.String(length=255), nullable=False),
    sa.Column('code2', sa.String(length=255), nullable=False),
    sa.Column('code3', sa.String(length=255), nullable=False),
    sa.Column('seller_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['seller_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product')
    op.drop_table('user')
    op.drop_table('supplier')
    # ### end Alembic commands ###