from app.models.definitions import Departments
from pydantic import BaseModel
from pydantic import conlist

class EmployeeRecord(BaseModel):
    id: int
    name: str
    datetime: str
    department_id: int
    job_id: int

class EmployeeBatch(BaseModel):
    records: conlist(EmployeeRecord, min_length=1, max_length=1000)

class DepartmentRecord(BaseModel):
    id: int
    department: str

class DepartmentBatch(BaseModel):
    records: conlist(DepartmentRecord, min_length=1, max_length=1000)

class JobRecord(BaseModel):
    id: int
    job: str

class JobBatch(BaseModel):
    records: conlist(JobRecord, min_length=1, max_length=1000)