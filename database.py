from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from api.settings import get_settings, get_settings2

Base_1 = declarative_base()
Base_2 = declarative_base()

SQLALCHEMY_DATABASE_URL = get_settings().db_dsn
SQLALCHEMY_DATABASE_URL2 = get_settings2().db_dsn

###multiple databases-1
engine1 = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal1 = sessionmaker(autocommit=False, autoflush=False, bind=engine1)

###multiple databases-2
engine2 = create_engine(SQLALCHEMY_DATABASE_URL2)
SessionLocal2 = sessionmaker(autocommit=False, autoflush=False, bind=engine2)

def get_db():
    session = SessionLocal1()
    try:
        yield session
        session.commit()
    finally:
        session.close()
        
def get_db2():
    session = SessionLocal2()
    try:
        yield session
        session.commit()
    finally:
        session.close()

