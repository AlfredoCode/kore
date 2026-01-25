import sys 
from pathlib import Path 

# add backend/ to PYTHONPATH 
ROOT = Path(__file__).resolve().parents[1] 
sys.path.insert(0, str(ROOT))

import os
import pytest
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.project.models import Project
from src.employee.models import Employee, EmployeeAllowedProject, EmployeeRoleType
from src.priority.models import Priority
from src.issue.models import Issue, IssueComment, IssueStatusHistory, IssueStatusType, IssueType
from src.database import Base

from src.database import Base
from dotenv import load_dotenv

load_dotenv()

TEST_DB_NAME = "kore_test"
TEST_DB_USER = os.getenv("DB_USER", "kore_user")
TEST_DB_PASSWORD = os.getenv("DB_PASSWORD", "kore_password")
TEST_DB_HOST = os.getenv("DB_HOST", "localhost")
TEST_DB_PORT = os.getenv("DB_PORT", "5432")

TEST_DB_URL = f"postgresql+psycopg2://{TEST_DB_USER}:{TEST_DB_PASSWORD}@{TEST_DB_HOST}:{TEST_DB_PORT}/{TEST_DB_NAME}"

@pytest.fixture(scope="session", autouse=True)
def create_test_database():
    conn = psycopg2.connect(
        dbname="postgres",
        user=TEST_DB_USER,
        password=TEST_DB_PASSWORD,
        host=TEST_DB_HOST,
        port=TEST_DB_PORT,
    )
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()

    cur.execute(f"SELECT 1 FROM pg_database WHERE datname = %s;", (TEST_DB_NAME,))
    exists = cur.fetchone()

    if not exists:
        print(f"Creating test database '{TEST_DB_NAME}'...")
        cur.execute(f"CREATE DATABASE {TEST_DB_NAME};")

    cur.close()
    conn.close()

@pytest.fixture(scope="session")
def db_engine(create_test_database):
    engine = create_engine(TEST_DB_URL)
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield engine
    Base.metadata.drop_all(bind=engine)

@pytest.fixture()
def db_session(db_engine):
    TestingSessionLocal = sessionmaker(bind=db_engine)
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.rollback()
        session.close()
