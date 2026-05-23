from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class Ticket(Base):

    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True)
    priority = Column(String(20))
    category = Column(String(100))
    sentiment = Column(String(50))
    confidence = Column(Integer)
    ai_summary = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)