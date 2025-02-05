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
    records: conlist(EmployeeRecord, min_items=1, max_items=1000)

class DepartmentRecord(BaseModel):
    id: int
    department: str

class DepartmentBatch(BaseModel):
    records: conlist(DepartmentRecord, min_items=1, max_items=1000)

class JobRecord(BaseModel):
    id: int
    job: str

class JobBatch(BaseModel):
    records: conlist(JobRecord, min_items=1, max_items=1000)