import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from tasks.config import main_settings


def get_database():
    session = local_session()
    try:
        yield session
    finally:
        session.close()


BASEDIR = os.path.dirname(os.path.abspath(__name__))
path_to_db = os.path.join(BASEDIR, 'tasks', 'database', 'DB')

if not os.path.exists(path_to_db):
    os.makedirs(path_to_db)

base = declarative_base()
enj = create_engine(
    main_settings.db_url,
    connect_args={'check_same_threads': False},
    echo=True,)

local_session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=enj)
