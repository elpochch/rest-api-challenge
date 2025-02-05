from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.db.main import init_db
from app.api.routes import employees_router, departments_router, jobs_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up")
    await init_db()
    yield
    print("Shutting down")

app = FastAPI(
    title="RestAPI de creación de registros en PostgreSQL",
    description="Esta es una RestAPI de creación de registros en PostgreSQL para la resolución del challenge",
    version="0.1",
    lifespan=lifespan
)

app.include_router(employees_router)
app.include_router(departments_router)
app.include_router(jobs_router)

@app.get("/")
async def root():
    return {"message": "Bienvenido a la RestAPI de creación de registros en PostgreSQL"}