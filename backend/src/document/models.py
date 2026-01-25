from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from src.database import Base

class Document(Base):
    __tablename__ = "Document"

    DocumentId = Column(Integer, primary_key=True)
    FileName = Column(String, nullable=False)
    FilePath = Column(String, nullable=False)
    Extension = Column(String(10), nullable=False)
    UploadedDate = Column(DateTime, nullable=False)
    UploadedByEmployeeId = Column(Integer, ForeignKey("Employee.EmployeeId"), nullable=False)
    IssueId = Column(Integer, ForeignKey("Issue.IssueId"), nullable=False)