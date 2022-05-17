from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from producer import config

DATABASE_URI = config.DATABASE_URI

engine = create_engine(
    DATABASE_URI, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
