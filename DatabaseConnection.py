from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

sql_database_url = "mysql://root:1234@localhost:3306/crud_fastapai"

engine = create_engine(sql_database_url)

sessionLocal = sessionmaker(autocommit=False, bind=engine)

base = declarative_base()
