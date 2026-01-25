from alembic import context
from sqlalchemy import create_engine
from sqlalchemy import pool
from logging.config import fileConfig
import os

from src.database import Base
# import your models to register metadata
from src.project.models import Project
from src.priority.models import Priority
from src.employee.models import Employee, EmployeeRoleType, EmployeeAllowedProject
from src.issue.models import Issue, IssueComment, IssueStatusHistory, IssueStatusType, IssueType

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata

def get_db_url(db_env_or_name, default=None):
    user = os.getenv("DB_USER", "kore_user")
    password = os.getenv("DB_PASSWORD", "kore_password")
    host = os.getenv("DB_HOST", "localhost")
    port = os.getenv("DB_PORT", "5432")

    # If default is provided, treat first param as env var name, else as direct DB name
    if default is not None:
        db = os.getenv(db_env_or_name, default)
    else:
        # no default means treat the argument as the actual DB name
        db = db_env_or_name

    return f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}"

def run_migrations_for_engine(engine):
    with engine.connect() as connection:
        print("Registered tables:", Base.metadata.tables.keys())

        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            # other context options here if needed
        )
        with context.begin_transaction():
            context.run_migrations()

def run_migrations_online() -> None:
    # Create engines for main and test dbs
    main_engine = create_engine(get_db_url("DB_NAME", "kore"), poolclass=pool.NullPool)
    test_engine = create_engine(get_db_url("kore_test"), poolclass=pool.NullPool)


    # Run migrations on main DB
    run_migrations_for_engine(main_engine)

    # Run migrations on test DB
    run_migrations_for_engine(test_engine)

def run_migrations_offline() -> None:
    # Offline mode is more complex for two DBs, so just run for main DB here
    url = get_db_url("DB_NAME", "kore")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
