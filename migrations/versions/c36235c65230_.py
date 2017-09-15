"""empty message

Revision ID: c36235c65230
Revises: c440ea467b01
Create Date: 2017-09-15 13:38:08.012760

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'c36235c65230'
down_revision = 'c440ea467b01'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ham_training_set',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('term', sa.String(length=255), nullable=True),
    sa.Column('value', sa.Integer(), nullable=True),
    sa.Column('created_timestamp', sa.DateTime(), nullable=True),
    sa.Column('updated_timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('term')
    )
    op.create_table('hoax_training_set',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('term', sa.String(length=255), nullable=True),
    sa.Column('value', sa.Integer(), nullable=True),
    sa.Column('created_timestamp', sa.DateTime(), nullable=True),
    sa.Column('updated_timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('term')
    )
    op.create_table('ow_base_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=128), nullable=True),
    sa.Column('username', sa.String(length=32), nullable=True),
    sa.Column('password', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stopwords',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('term', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('term')
    )
    op.create_table('feedback',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=255), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('vote', sa.Integer(), nullable=True),
    sa.Column('reason', sa.Text(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('ip_address', sa.Text(), nullable=True),
    sa.Column('created_timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ham_count',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('qty', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('created_timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('hoax_count',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('qty', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('created_timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # op.drop_table('entry')
    # op.drop_table('comment')
    # op.drop_table('entry_tags')
    # op.drop_table('tag')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tag',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('tag_id_seq'::regclass)"), nullable=False),
    sa.Column('name', sa.VARCHAR(length=64), autoincrement=False, nullable=True),
    sa.Column('slug', sa.VARCHAR(length=64), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='tag_pkey'),
    sa.UniqueConstraint('slug', name='tag_slug_key'),
    postgresql_ignore_search_path=False
    )
    op.create_table('entry_tags',
    sa.Column('tag_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('entry_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['entry_id'], ['entry.id'], name='entry_tags_entry_id_fkey'),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], name='entry_tags_tag_id_fkey')
    )
    op.create_table('comment',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=64), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(length=64), autoincrement=False, nullable=True),
    sa.Column('url', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('ip_address', sa.VARCHAR(length=64), autoincrement=False, nullable=True),
    sa.Column('body', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('status', sa.SMALLINT(), autoincrement=False, nullable=True),
    sa.Column('created_timestamp', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('entry_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['entry_id'], ['entry.id'], name='comment_entry_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='comment_pkey')
    )
    op.create_table('entry',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('slug', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('body', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('status', sa.SMALLINT(), server_default=sa.text("'0'::smallint"), autoincrement=False, nullable=True),
    sa.Column('create_timestamp', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('modified_timestamp', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('author_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], name='entry_author_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='entry_pkey'),
    sa.UniqueConstraint('slug', name='entry_slug_key')
    )
    op.drop_table('hoax_count')
    op.drop_table('ham_count')
    op.drop_table('feedback')
    op.drop_table('stopwords')
    op.drop_table('ow_base_user')
    op.drop_table('hoax_training_set')
    op.drop_table('ham_training_set')
    # ### end Alembic commands ###