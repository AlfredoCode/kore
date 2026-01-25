from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from src.database import Base

class Employee(Base):
    __tablename__ = "Employee"

    EmployeeId = Column(Integer, primary_key=True)
    FirstName = Column(String(50), nullable=False)
    SecondName = Column(String(20), nullable=False)
    EmployeeRoleTypeId = Column(Integer, ForeignKey('EmployeeRoleType.EmployeeRoleTypeId'), nullable=False)
    Email = Column(String(40), nullable=False, unique=True)
    PassHash = Column(String(255), nullable=False)
    CreatedDate = Column(DateTime, nullable=False)
    ModifiedDate = Column(DateTime, nullable=True)
    EmployeeSupervisorId = Column(Integer, ForeignKey('Employee.EmployeeId'), nullable=True)
    SystemAccess = Column(Boolean, nullable=False, default=0)

class EmployeeRoleType(Base):
    __tablename__ = "EmployeeRoleType"
    
    EmployeeRoleTypeId = Column(Integer, primary_key=True)
    Description = Column(String(50), nullable=False, unique=True)
    Active = Column(Boolean, nullable=False, default=0)

class EmployeeAllowedProject(Base):
    __tablename__ = "EmployeeAllowedProject"
    
    EmployeeAllowedProjectId = Column(Integer, primary_key=True)
    EmployeeId = Column(Integer, ForeignKey('Employee.EmployeeId'), nullable=False)
    ProjectId = Column(Integer, ForeignKey('Project.ProjectId'), nullable=False)
    AllowedAccessDate = Column(DateTime, nullable=False)
    RemovedAccessDate = Column(DateTime, nullable=True)

class EmployeeIssue(Base):
    __tablename__ = "EmployeeIssue"
    
    EmployeeIssueId = Column(Integer, primary_key=True)
    EmployeeId = Column(Integer, ForeignKey("Employee.EmployeeId"), nullable=False)
    IssueId = Column(Integer, ForeignKey("Issue.IssueId"), nullable=False)
    AssignedDate = Column(DateTime, nullable=False)
    UnassignedDate = Column(DateTime, nullable=True)
  
