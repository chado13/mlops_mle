"""empty message

Revision ID: 56edcc7d1bca
Revises: 
Create Date: 2023-03-18 15:31:48.279856

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56edcc7d1bca'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('iris_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('sepal_length', sa.Float(), nullable=True),
    sa.Column('sepal_width', sa.Float(), nullable=True),
    sa.Column('petal_length', sa.Float(), nullable=True),
    sa.Column('petal_width', sa.Float(), nullable=True),
    sa.Column('target', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('iris_data')
    # ### end Alembic commands ###
