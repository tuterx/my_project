"""empty message

Revision ID: 851683b28dcc
Revises: 45d18cd22f29
Create Date: 2023-02-08 17:50:00.984447

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '851683b28dcc'
down_revision = '45d18cd22f29'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('email_capthca',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('capthca', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('email_capthca')
    # ### end Alembic commands ###
