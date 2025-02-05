from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.main import get_session
from http import HTTPStatus

employees_router = APIRouter(prefix="/employees", tags=["Employees"])

@employees_router.get("/")
async def get_employees(session: AsyncSession = Depends(get_session)):
    pass

@employees_router.post("/", status_code=HTTPStatus.CREATED)
async def create_employees(session: AsyncSession = Depends(get_session)):
    pass

@employees_router.get("/{employee_id}", status_code=HTTPStatus.OK)
async def get_employee(employee_id: int, session: AsyncSession = Depends(get_session)):
    pass

@employees_router.put("/{employee_id}", status_code=HTTPStatus.OK)
async def update_employee(employee_id: int, session: AsyncSession = Depends(get_session)):
    pass

@employees_router.delete("/{employee_id}", status_code=HTTPStatus.NO_CONTENT)
async def delete_employee(employee_id: int, session: AsyncSession = Depends(get_session)):
    pass