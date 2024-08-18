"""Update relationships between ChatbotUserModel and ChatbotChatModel

Revision ID: 1a456341c027
Revises: ad2b6289f32f
Create Date: 2024-08-13 12:33:16.888584

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1a456341c027'
down_revision: Union[str, None] = 'ad2b6289f32f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Drop the old foreign key constraint
    op.drop_constraint('chatbot_interactions_user_id_fkey', 'chatbot_interactions', type_='foreignkey')
    
    # Create the new foreign key constraint linking chatbot_interactions.user_id to chatbot_users.id
    op.create_foreign_key(None, 'chatbot_interactions', 'chatbot_users', ['user_id'], ['id'])

    # No need to add profile_picture and preferences columns since they already exist
    # op.add_column('chatbot_users', sa.Column('profile_picture', sa.String(), nullable=True))
    # op.add_column('chatbot_users', sa.Column('preferences', sa.String(), nullable=True))

def downgrade() -> None:
    # Reverse the addition of new columns (if they had been added)
    # op.drop_column('chatbot_users', 'preferences')
    # op.drop_column('chatbot_users', 'profile_picture')
    
    # Drop the new foreign key constraint
    op.drop_constraint(None, 'chatbot_interactions', type_='foreignkey')
    
    # Recreate the old foreign key constraint linking chatbot_interactions.user_id to users.id
    op.create_foreign_key('chatbot_interactions_user_id_fkey', 'chatbot_interactions', 'users', ['user_id'], ['id'])
