"""empty message

Revision ID: 4119075ad777
Revises: 06cbf9ec1e45
Create Date: 2024-01-21 17:26:30.430862

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4119075ad777'
down_revision = '06cbf9ec1e45'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todos', schema=None) as batch_op:
        batch_op.add_column(sa.Column('complete', sa.Boolean(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todos', schema=None) as batch_op:
        batch_op.drop_column('complete')

    # ### end Alembic commands ###
