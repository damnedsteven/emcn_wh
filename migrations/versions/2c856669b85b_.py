"""empty message

Revision ID: 2c856669b85b
Revises: 69b764dfd001
Create Date: 2017-03-10 00:01:07.751346

"""

# revision identifiers, used by Alembic.
revision = '2c856669b85b'
down_revision = '69b764dfd001'

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