"""empty message

Revision ID: 96f58fdbc477
Revises: 2c5d9595ca46
Create Date: 2019-10-15 19:25:47.943566

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96f58fdbc477'
down_revision = '2c5d9595ca46'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('solution', sa.Column('date_submitted', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('solution', 'date_submitted')
    # ### end Alembic commands ###
