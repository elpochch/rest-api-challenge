from pydantic import BaseModel, validator

class HiredEmployees(BaseModel):
    """
    #TODO: Add description
    """
    id: int
    name: str
    datetime: str
    department_id: int
    job_id: int

class Departments(BaseModel):
    """
    :TODO: Add description
    """
    id: int
    department: str

class Jobs(BaseModel):
    """
    :TODO Add description
    """
    id: int
    job: str