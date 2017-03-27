"""empty message

Revision ID: 74077fd77c39
Revises: ad8e0c01efad
Create Date: 2017-03-09 23:55:16.815986

"""

# revision identifiers, used by Alembic.
revision = '74077fd77c39'
down_revision = 'ad8e0c01efad'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    # ### end Alembic commands ###