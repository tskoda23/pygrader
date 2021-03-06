"""solutions table

Revision ID: 3abce4b17caf
Revises: 923e7084fa75
Create Date: 2019-05-14 23:54:14.621489

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '3abce4b17caf'
down_revision = '923e7084fa75'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('assignment_ibfk_4', 'assignment', type_='foreignkey')
    op.drop_column('assignment', 'default_solution_id')
    op.add_column('solution', sa.Column('assignment_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'solution', 'assignment', ['assignment_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'solution', type_='foreignkey')
    op.drop_column('solution', 'assignment_id')
    op.add_column('assignment', sa.Column('default_solution_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.create_foreign_key('assignment_ibfk_4', 'assignment', 'solution', ['default_solution_id'], ['id'])
    # ### end Alembic commands ###
