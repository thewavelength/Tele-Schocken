"""add gamestatistics

Revision ID: 980580d8d3f1
Revises: 061f0bf664d7
Create Date: 2020-05-01 18:59:41.896812

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '980580d8d3f1'
down_revision = '061f0bf664d7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('statistic',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('usercount', sa.Integer(), nullable=True),
    sa.Column('halfcount', sa.Integer(), nullable=True),
    sa.Column('started', sa.DateTime(), nullable=True),
    sa.Column('refreshed', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('game', sa.Column('halfcount', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('game', 'halfcount')
    op.drop_table('statistic')
    # ### end Alembic commands ###
