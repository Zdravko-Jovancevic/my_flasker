"""added username

Revision ID: 086d0bbfc76d
Revises: f96facd92081
Create Date: 2022-07-07 03:26:06.149875

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '086d0bbfc76d'
down_revision = 'f96facd92081'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('username', sa.String(length=20), nullable=False))
    op.create_unique_constraint(None, 'users', ['username'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('users', 'username')
    # ### end Alembic commands ###
