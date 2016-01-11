from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
followers = Table('followers', post_meta,
    Column('follower_id', Integer),
    Column('followed_id', Integer),
)

user = Table('user', pre_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('nickname', String),
    Column('fullname', String),
    Column('email', String),
    Column('about_me', String),
    Column('last_seen', DateTime),
    Column('test', String),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['followers'].create()
    pre_meta.tables['user'].columns['fullname'].drop()
    pre_meta.tables['user'].columns['test'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['followers'].drop()
    pre_meta.tables['user'].columns['fullname'].create()
    pre_meta.tables['user'].columns['test'].create()
