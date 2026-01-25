import pytest
from datetime import datetime
from sqlalchemy.exc import IntegrityError
from src.employee.models import Employee, EmployeeRoleType

@pytest.fixture
def admin_role(db_session):
    role = db_session.query(EmployeeRoleType).filter_by(Description="Admin").first()
    if not role:
        role = EmployeeRoleType(Description="Admin", Active=True)
        db_session.add(role)
        db_session.commit()
        db_session.refresh(role)
    return role

def test_employee_ok(db_session, admin_role):
    employee = Employee(
        FirstName="John",
        SecondName="Doe",
        EmployeeRoleTypeId=admin_role.EmployeeRoleTypeId,
        Email="john@test.com",
        PassHash="hash",
        SystemAccess=True,
        CreatedDate=datetime.now()
    )
    db_session.add(employee)
    db_session.commit()
    db_session.refresh(employee)

    assert employee.EmployeeId is not None
    assert employee.Email == "john@test.com"

def test_employee_invalid_role(db_session, admin_role):
    invalid_role_id = admin_role.EmployeeRoleTypeId + 9999
    employee = Employee(
        FirstName="John",
        SecondName="Doe",
        EmployeeRoleTypeId=invalid_role_id,
        Email="john_invalid@test.com",
        PassHash="hash",
        SystemAccess=True,
        CreatedDate=datetime.now()
    )
    db_session.add(employee)
    with pytest.raises(IntegrityError):
        db_session.commit()
    db_session.rollback()
    exists = db_session.query(Employee).filter_by(Email="john_invalid@test.com").first()
    assert exists is None

def test_employee_missing_required_field(db_session, admin_role):
    # Missing FirstName (required)
    employee = Employee(
        SecondName="Doe",
        EmployeeRoleTypeId=admin_role.EmployeeRoleTypeId,
        Email="missing_first@test.com",
        PassHash="hash",
        SystemAccess=True,
        CreatedDate=datetime.now()
    )
    db_session.add(employee)
    with pytest.raises(IntegrityError):
        db_session.commit()
    db_session.rollback()

def test_employee_duplicate_email(db_session, admin_role):
    # Create first employee with email
    emp1 = Employee(
        FirstName="Jane",
        SecondName="Smith",
        EmployeeRoleTypeId=admin_role.EmployeeRoleTypeId,
        Email="duplicate@test.com",
        PassHash="hash1",
        SystemAccess=True,
        CreatedDate=datetime.now()
    )
    db_session.add(emp1)
    db_session.commit()

    # Try to create second employee with same email
    emp2 = Employee(
        FirstName="Jake",
        SecondName="Smith",
        EmployeeRoleTypeId=admin_role.EmployeeRoleTypeId,
        Email="duplicate@test.com",
        PassHash="hash2",
        SystemAccess=True,
        CreatedDate=datetime.now()
    )
    db_session.add(emp2)
    with pytest.raises(IntegrityError):
        db_session.commit()
    db_session.rollback()

def test_employee_update_fields(db_session, admin_role):
    employee = Employee(
        FirstName="Alice",
        SecondName="Johnson",
        EmployeeRoleTypeId=admin_role.EmployeeRoleTypeId,
        Email="alice@test.com",
        PassHash="initialhash",
        SystemAccess=False,
        CreatedDate=datetime.now()
    )
    db_session.add(employee)
    db_session.commit()
    db_session.refresh(employee)

    # Update fields
    employee.PassHash = "newhash"
    employee.SystemAccess = True
    employee.ModifiedDate = datetime.now()

    db_session.commit()
    db_session.refresh(employee)

    assert employee.PassHash == "newhash"
    assert employee.SystemAccess is True
    assert employee.ModifiedDate is not None

def test_employee_supervisor_relationship(db_session, admin_role):
    supervisor = Employee(
        FirstName="John",
        SecondName="The Supervisor",
        EmployeeRoleTypeId=admin_role.EmployeeRoleTypeId,
        Email="supervisor@test.com",
        PassHash="hash",
        SystemAccess=True,
        CreatedDate=datetime.now()
    )
    db_session.add(supervisor)
    db_session.commit()
    db_session.refresh(supervisor)

    employee = Employee(
        FirstName="Andy",
        SecondName="Doe",
        EmployeeRoleTypeId=admin_role.EmployeeRoleTypeId,
        Email="Andy@test.com",
        PassHash="hash",
        SystemAccess=True,
        CreatedDate=datetime.now(),
        EmployeeSupervisorId=supervisor.EmployeeId
    )
    db_session.add(employee)
    db_session.commit()
    db_session.refresh(employee)

    assert employee.EmployeeSupervisorId == supervisor.EmployeeId
