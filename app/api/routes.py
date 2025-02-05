from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.main import get_session
from http import HTTPStatus

employees_router = APIRouter(prefix="/employees", tags=["Employees"])
@employees_router.post("/", status_code=HTTPStatus.CREATED)
async def create_employees(session: AsyncSession = Depends(get_session)):
    pass

departments_router = APIRouter(prefix="/departments", tags=["Departments"])

@departments_router.post("/", status_code=HTTPStatus.CREATED)
async def create_departments(session: AsyncSession = Depends(get_session)):
    pass

jobs_router = APIRouter(prefix="/jobs", tags=["Jobs"])
@jobs_router.post("/", status_code=HTTPStatus.CREATED)
async def create_jobs(session: AsyncSession = Depends(get_session)):
    pass