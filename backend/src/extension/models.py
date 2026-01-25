from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from src.database import Base

class Extension(Base):
    __tablename__ = "Extension"

    ExtensionId = Column(Integer, primary_key=True)
    Shortcut = Column(String(10), nullable=False, unique=True)
    CreatedByEmployeeId = Column(Integer, ForeignKey("Employee.EmployeeId"), nullable=False)
    CreatedDate = Column(DateTime, nullable=False)
    DeactivatedDate = Column(DateTime, nullable=True)
    MaxFileSize = Column(Integer, nullable=False, default=10)