"""empty message

Revision ID: b300f479cf1e
Revises: e99422f251dc
Create Date: 2017-12-13 09:37:34.490743

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b300f479cf1e'
down_revision = 'e99422f251dc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ohho_user_favourite_book', sa.Column('url', sa.String(length=256), nullable=True))
    op.add_column('ohho_user_favourite_movie', sa.Column('casts', sa.String(length=128), nullable=True))
    op.add_column('ohho_user_favourite_movie', sa.Column('genres', sa.String(length=128), nullable=True))
    op.add_column('ohho_user_favourite_movie', sa.Column('icon', sa.String(length=256), nullable=True))
    op.add_column('ohho_user_favourite_movie', sa.Column('url', sa.String(length=256), nullable=True))
    op.add_column('ohho_user_favourite_music', sa.Column('icon', sa.String(length=256), nullable=True))
    op.add_column('ohho_user_favourite_music', sa.Column('url', sa.String(length=256), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('ohho_user_favourite_music', 'url')
    op.drop_column('ohho_user_favourite_music', 'icon')
    op.drop_column('ohho_user_favourite_movie', 'url')
    op.drop_column('ohho_user_favourite_movie', 'icon')
    op.drop_column('ohho_user_favourite_movie', 'genres')
    op.drop_column('ohho_user_favourite_movie', 'casts')
    op.drop_column('ohho_user_favourite_book', 'url')
    # ### end Alembic commands ###
