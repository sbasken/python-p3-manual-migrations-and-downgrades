"""Renaming students to scholars

Revision ID: 6357e59719f1
Revises: 791279dd0760
Create Date: 2023-03-25 09:22:17.101077

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6357e59719f1'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
