"""initial migration

Revision ID: 155b3b3f1710
Revises: 
Create Date: 2024-10-18 17:49:33.113589

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '155b3b3f1710'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create the users table with a registered_at field that defaults to the current time
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('nickname', sa.String),
        sa.Column('email', sa.String, unique=True, nullable=False),
        sa.Column('hashed_password', sa.String, nullable=False),
        sa.Column('registered_at', sa.DateTime, server_default=sa.func.now(), nullable=False),
    )

def downgrade() -> None:
    # Drop the users table
    op.drop_table('users')
