from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from src.database import Base

class Project(Base):
    __tablename__ = "Project"
    
    ProjectId = Column(Integer, primary_key=True)
    Title = Column(String(40), nullable=False)
    Description = Column(String(255), nullable=True)
    CreatedDate = Column(DateTime, nullable=False)
    CreatedByEmployeeId = Column(Integer, ForeignKey('Employee.EmployeeId'), nullable=True)
    Active = Column(Boolean, nullable=False, default=0)



    
    