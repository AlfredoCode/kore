import os
from logging.config import fileConfig

from sqlalchemy import create_engine
from sqlalchemy import pool

from alembic import context
from src.project.models import Project
from src.priority.models import Priority
from src.employee.models import Employee, EmployeeAllowedProject, EmployeeRoleType
from src.issue.models import Issue, IssueComment, IssueStatusHistory, IssueStatusType, IssueType
from src.database import Base
from sqlalchemy.orm import Session
# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.
def get_url():
    user = os.getenv("DB_USER", "kore_user")
    password = os.getenv("DB_PASSWORD", "kore_password")
    host = os.getenv("DB_HOST", "localhost")
    port = os.getenv("DB_PORT", "5432")
    db = os.getenv("DB_NAME", "kore")
    return f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}"

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = get_url()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()
def seed_employee_roles(connection):
    """Insert initial EmployeeRoleType rows if table is empty."""
    session = Session(bind=connection)
    try:
        # Check if table already has data
        exists = session.query(EmployeeRoleType).first()
        if not exists:
            roles = [
                EmployeeRoleType(Title="Administrator", Description="Administrator role with full access", Active=1),
                EmployeeRoleType(Title="Manager", Description="Manager role with project access", Active=1),
                EmployeeRoleType(Title="Developer", Description="Developer role with issue handling", Active=1),
                EmployeeRoleType(Title="Tester", Description="Tester role for QA purposes", Active=1),
                EmployeeRoleType(Title="User", Description="Default user role", Active=1),
            ]
            session.add_all(roles)
            session.commit()
    finally:
        session.close()
def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = create_engine(get_url(), poolclass=pool.NullPool)

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )
        # Recreate all tables
        Base.metadata.drop_all(bind=connection)
        Base.metadata.create_all(bind=connection)
        with context.begin_transaction():
            context.run_migrations()
        seed_employee_roles(connection)


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

