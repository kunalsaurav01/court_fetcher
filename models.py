from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class QueryLog(Base):
    __tablename__ = 'querylog'
    id = Column(Integer, primary_key=True)
    case_type = Column(String)
    case_number = Column(String)
    filing_year = Column(String)
    court = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
    raw_response = Column(Text)

engine = create_engine('sqlite:///db.sqlite3')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
