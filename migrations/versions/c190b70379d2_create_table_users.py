"""create table users

Revision ID: c190b70379d2
Revises: ae34635ed36d
Create Date: 2022-07-05 18:29:56.813737

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'c190b70379d2'
down_revision = 'ae34635ed36d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('login', sa.Unicode(), nullable=True),
                    sa.Column('password', sa.Unicode(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
