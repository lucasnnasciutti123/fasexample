"""add content column to post tables

Revision ID: ba429e7440f8
Revises: 3355c7af4b5d
Create Date: 2026-02-08 13:33:51.168416

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ba429e7440f8'
down_revision: Union[str, Sequence[str], None] = '3355c7af4b5d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column("posts",sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts','content')
    pass
