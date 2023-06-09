"""Create puppies table

Revision ID: 699d670cb5fc
Revises: 
Create Date: 2023-02-19 20:26:31.063376

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '699d670cb5fc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('puppies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('puppies')
    # ### end Alembic commands ###
