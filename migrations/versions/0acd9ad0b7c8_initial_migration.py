"""initial migration

Revision ID: 0acd9ad0b7c8
Revises: 
Create Date: 2019-10-25 19:40:58.536098

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0acd9ad0b7c8'
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
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('supplier')
    # ### end Alembic commands ###