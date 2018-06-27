
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from flask import Flask

from mappings.characters_mapping import Base

Session = sessionmaker(autoflush=False)



db_uri = 'sqlite:///database3.db'
engine = create_engine(db_uri)
conn = engine.connect()
Base.metadata.create_all(engine)

Session.configure(bind=engine)

def get_session():
    return Session()

