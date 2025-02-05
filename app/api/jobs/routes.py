from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.main import get_session
from http import HTTPStatus

jobs_router = APIRouter(prefix="/jobs", tags=["Jobs"])

@jobs_router.get("/")
async def get_jobs(session: AsyncSession = Depends(get_session)):
    pass

@jobs_router.post("/", status_code=HTTPStatus.CREATED)
async def create_jobs(session: AsyncSession = Depends(get_session)):
    pass

@jobs_router.get("/{job_id}", status_code=HTTPStatus.OK)
async def get_job(job_id: int, session: AsyncSession = Depends(get_session)):
    pass

@jobs_router.put("/{job_id}", status_code=HTTPStatus.OK)
async def update_job(job_id: int, session: AsyncSession = Depends(get_session)):
    pass

@jobs_router.delete("/{job_id}", status_code=HTTPStatus.NO_CONTENT)
async def delete_job(job_id: int, session: AsyncSession = Depends(get_session)):
    pass