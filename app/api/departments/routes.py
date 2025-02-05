from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.main import get_session
from http import HTTPStatus

departments_router = APIRouter(prefix="/departments", tags=["Departments"])

@departments_router.get("/")
async def get_departments(session: AsyncSession = Depends(get_session)):
    pass

@departments_router.post("/", status_code=HTTPStatus.CREATED)
async def create_departments(session: AsyncSession = Depends(get_session)):
    pass

@departments_router.get("/{department_id}", status_code=HTTPStatus.OK)
async def get_department(department_id: int, session: AsyncSession = Depends(get_session)):
    pass

@departments_router.put("/{department_id}", status_code=HTTPStatus.OK)
async def update_department(department_id: int, session: AsyncSession = Depends(get_session)):
    pass

@departments_router.delete("/{department_id}", status_code=HTTPStatus.NO_CONTENT)
async def delete_department(department_id: int, session: AsyncSession = Depends(get_session)):
    pass