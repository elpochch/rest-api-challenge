from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.main import get_session
from http import HTTPStatus
from .schemas import EmployeeBatch, DepartmentBatch, JobBatch
from app.services.transactions_service import EmployeeService, DepartmentService, JobService

employees_router = APIRouter(prefix="/employees", tags=["Employees"])
@employees_router.post("/", status_code=HTTPStatus.CREATED)
async def create_employees(employees_data: EmployeeBatch,session: AsyncSession = Depends(get_session)):
    insert_employees_batch = await EmployeeService(session).create_employees(employees_data)
    return insert_employees_batch

departments_router = APIRouter(prefix="/departments", tags=["Departments"])

@departments_router.post("/", status_code=HTTPStatus.CREATED, response_model=dict)
async def create_departments(departments_data:DepartmentBatch, session: AsyncSession = Depends(get_session)):
    insert_departments_batch = await DepartmentService(session).create_departments(departments_data)
    return insert_departments_batch

jobs_router = APIRouter(prefix="/jobs", tags=["Jobs"])
@jobs_router.post("/", status_code=HTTPStatus.CREATED)
async def create_jobs(jobs_data: JobBatch ,session: AsyncSession = Depends(get_session)):
    insert_jobs_batch = await JobService(session).create_jobs(jobs_data)
    return insert_jobs_batch