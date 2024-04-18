from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

sql_database_url = "postgres://crud_api_fast_user:e0X89N0xEsW264IWJfZYpzkIGZo1SB1Q@dpg-cogn2fo21fec73bj2if0-a/crud_api_fast"

engine = create_engine(sql_database_url)

sessionLocal = sessionmaker(autocommit=False, bind=engine)

base = declarative_base()
