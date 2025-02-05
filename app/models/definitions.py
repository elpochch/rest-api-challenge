from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class HiredEmployees(Base):
    """
    #TODO: Add description
    """
    __tablename__ = "hired_employees"
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String, nullable=False)
    datetime = Column('datetime', String, nullable=False)
    department_id = Column('department_id', Integer, nullable=False)
    job_id = Column('job_id', Integer, nullable=False)

class Departments(Base):
    """
    :TODO: Add description
    """
    __tablename__ = "departments"
    id = Column('id',Integer, primary_key=True)
    department = Column('department', String, nullable=False)

class Jobs(Base):
    """
    :TODO Add description
    """
    __tablename__ = "jobs"
    id = Column('id', Integer, primary_key=True)
    job = Column('job', String, nullable=False)