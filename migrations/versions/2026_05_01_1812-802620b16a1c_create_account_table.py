"""create account table

Revision ID: 802620b16a1c
Revises: 
Create Date: 2026-05-01 18:12:42.124350

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '802620b16a1c'
down_revision = None
branch_labels = ["alembic.sqlalchemy.org", "tutorial"]
depends_on = None

def upgrade():
    op.create_table(
        'account',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200)),
    )

def downgrade():
    op.drop_table('account')
