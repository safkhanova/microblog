"""new fields in user model

Revision ID: 825818c3d4c0
Revises: b70fa43dc1af
Create Date: 2021-09-16 22:52:30.199191

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '825818c3d4c0'
down_revision = 'b70fa43dc1af'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
