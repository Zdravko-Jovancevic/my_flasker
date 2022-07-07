"""add foreign key

Revision ID: b40b8e7b4876
Revises: 086d0bbfc76d
Create Date: 2022-07-07 17:50:22.516991

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b40b8e7b4876'
down_revision = '086d0bbfc76d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('poster_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'posts', 'users', ['poster_id'], ['id'])
    op.drop_column('posts', 'author')
    op.create_unique_constraint(None, 'users', ['username'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.add_column('posts', sa.Column('author', sa.VARCHAR(length=255), nullable=True))
    op.drop_constraint(None, 'posts', type_='foreignkey')
    op.drop_column('posts', 'poster_id')
    # ### end Alembic commands ###