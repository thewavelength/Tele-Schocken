"""add fallling_dice_count to statistic

Revision ID: 50f1ca070417
Revises: b3e319ef9563
Create Date: 2020-05-17 15:17:49.889793

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50f1ca070417'
down_revision = 'b3e319ef9563'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('game', sa.Column('fallling_dice_count', sa.Integer(), nullable=True))
    op.add_column('statistic', sa.Column('fallling_dice_count', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('statistic', 'fallling_dice_count')
    op.drop_column('game', 'fallling_dice_count')
    # ### end Alembic commands ###
