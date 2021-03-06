"""solutions table

Revision ID: 923e7084fa75
Revises: 06dbffc5694f
Create Date: 2019-05-14 23:36:35.868335

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '923e7084fa75'
down_revision = '06dbffc5694f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('assignment', sa.Column('default_solution_id', sa.Integer(), nullable=True))
    op.drop_constraint('assignment_ibfk_2', 'assignment', type_='foreignkey')
    op.create_foreign_key(None, 'assignment', 'solution', ['default_solution_id'], ['id'])
    op.drop_column('assignment', 'solution_id')
    op.drop_constraint('course_ibfk_1', 'course', type_='foreignkey')
    op.drop_column('course', 'creator_id')
    op.add_column('solution', sa.Column('is_default', sa.Boolean(), nullable=True))
    op.drop_column('solution', 'is_completed')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('solution', sa.Column('is_completed', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.drop_column('solution', 'is_default')
    op.add_column('course', sa.Column('creator_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.create_foreign_key('course_ibfk_1', 'course', 'user', ['creator_id'], ['id'])
    op.add_column('assignment', sa.Column('solution_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'assignment', type_='foreignkey')
    op.create_foreign_key('assignment_ibfk_2', 'assignment', 'solution', ['solution_id'], ['id'])
    op.drop_column('assignment', 'default_solution_id')
    # ### end Alembic commands ###
