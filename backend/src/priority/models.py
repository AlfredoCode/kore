from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from src.database import Base

class Priority(Base):
    __tablename__ = "Priority"

    PriorityId = Column(Integer, primary_key=True)
    Value = Column(Integer, nullable=False)