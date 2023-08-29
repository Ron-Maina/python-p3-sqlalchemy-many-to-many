"""Add game_user Association Table

Revision ID: 472b160c5546
Revises: b9c75fc765e8
Create Date: 2023-08-29 22:25:47.142028

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '472b160c5546'
down_revision = 'b9c75fc765e8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('game_users',
    sa.Column('game_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['game_id'], ['games.id'], name=op.f('fk_game_users_game_id_games')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_game_users_user_id_users')),
    sa.PrimaryKeyConstraint('game_id', 'user_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('game_users')
    # ### end Alembic commands ###
