"""empty message

Revision ID: 1ce7d779c808
Revises: cca39c7a863f
Create Date: 2018-02-19 12:04:29.536356

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1ce7d779c808'
down_revision = 'cca39c7a863f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('event_event_type_id_fkey', 'event', type_='foreignkey')
    op.drop_constraint('event_device_id_fkey', 'event', type_='foreignkey')
    op.create_foreign_key(None, 'event', 'device', ['device_id'], ['id'], onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(None, 'event', 'event_type', ['event_type_id'], ['id'], onupdate='CASCADE', ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'event', type_='foreignkey')
    op.drop_constraint(None, 'event', type_='foreignkey')
    op.create_foreign_key('event_device_id_fkey', 'event', 'device', ['device_id'], ['id'])
    op.create_foreign_key('event_event_type_id_fkey', 'event', 'event_type', ['event_type_id'], ['id'])
    # ### end Alembic commands ###
