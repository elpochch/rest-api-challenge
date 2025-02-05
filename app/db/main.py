from sqlalchemy import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from app.config import Settings
from models.definitions import Base

async_engine = create_async_engine(Settings.POSTGRES_URL, echo=True)

async def init_db():
    async with AsyncSession(async_engine) as session:
        async with session.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

async def get_session() -> AsyncSession:
    async_session = sessionmaker(
        bind=async_engine,
        class_=AsyncSession,
        expire_on_commit=False
    )
    async with async_session() as session:
        yield session