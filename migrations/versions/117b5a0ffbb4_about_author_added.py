"""about author added

Revision ID: 117b5a0ffbb4
Revises: b40b8e7b4876
Create Date: 2022-07-07 22:39:38.923929

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '117b5a0ffbb4'
down_revision = 'b40b8e7b4876'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'posts', 'users', ['poster_id'], ['id'])
    op.drop_column('posts', 'author')
    op.add_column('users', sa.Column('about_author', sa.Text(length=500), nullable=True))
    op.create_unique_constraint(None, 'users', ['username'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('users', 'about_author')
    op.add_column('posts', sa.Column('author', sa.VARCHAR(length=255), nullable=True))
    op.drop_constraint(None, 'posts', type_='foreignkey')
    # ### end Alembic commands ###
