from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la RestAPI de migración de archivos CSV a PostgreSQL"}