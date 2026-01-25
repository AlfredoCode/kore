from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from src.database import Base

class Issue(Base):
    __tablename__ = "Issue"

    IssueId = Column(Integer, primary_key=True)
    Title = Column(String(50), nullable=False)
    CreatedByEmployee = Column(Integer, ForeignKey("Employee.EmployeeId"), nullable=False)
    IssueTypeId = Column(Integer, ForeignKey("IssueType.IssueTypeId"), nullable=False)
    IssueStatusTypeId = Column(Integer, ForeignKey("IssueStatusType.IssueStatusTypeId"), nullable=False)
    StoryPoints = Column(Integer, nullable=True)
    PriorityId = Column(Integer, ForeignKey("Priority.PriorityId"), nullable=False)
    ProjectId = Column(Integer, ForeignKey("Project.ProjectId"), nullable=True)

class IssueType(Base):
    __tablename__ = "IssueType"

    IssueTypeId = Column(Integer, primary_key=True)
    Title = Column(String(50), nullable=False, unique=True)
    TagHexColor = Column(String(7), nullable=False, default="#ffffff")
    ModifiedByEmployeeId = Column(Integer, ForeignKey("Employee.EmployeeId"), nullable=True)
    CreatedByEmployeeId = Column(Integer, ForeignKey("Employee.EmployeeId"), nullable=False)

class IssueStatusType(Base):
    __tablename__ = "IssueStatusType"

    IssueStatusTypeId = Column(Integer, primary_key=True)
    Title = Column(String(30), nullable=False, unique=True)
    TagHexColor = Column(String(7), nullable=False, default="#ffffff")
    ModifiedByEmployeeId = Column(Integer, ForeignKey("Employee.EmployeeId"), nullable=True)
    CreatedByEmployeeId = Column(Integer, ForeignKey("Employee.EmployeeId"), nullable=False)

class IssueComment(Base):
    __tablename__ = "IssueComment"

    IssueCommentId = Column(Integer, primary_key=True)
    CommentedByEmployeeId = Column(Integer, ForeignKey("Employee.EmployeeId"), nullable=False)
    CommentDate = Column(DateTime, nullable=False)
    Content = Column(String, nullable=False)
    FilesIncluded = Column(Boolean, nullable=False, default=0)

class IssueStatusHistory(Base):
    __tablename__ = "IssueStatusHistory"
    IssueStatusHistoryId = Column(Integer, primary_key=True)
    IssueId = Column(Integer, nullable=False)
    IssueTitle = Column(String, nullable=False)
    IssueStatusTypeId = Column(Integer, nullable=False)
    IssueStatusTitle = Column(String, nullable=False)
    ModifiedByEmployeeId = Column(Integer, nullable=False)
    ModifiedByEmployeeName = Column(String, nullable=False)
    Priority = Column(Integer, nullable=False)
    ProjectId = Column(Integer, nullable=True)
    StoryPoints = Column(Integer, nullable=True)
