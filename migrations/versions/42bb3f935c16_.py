"""empty message

Revision ID: 42bb3f935c16
Revises: b6ad7cea65b0
Create Date: 2019-09-01 17:11:26.299544

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42bb3f935c16'
down_revision = 'b6ad7cea65b0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('solution', sa.Column('result_text', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('solution', 'result_text')
    # ### end Alembic commands ###
