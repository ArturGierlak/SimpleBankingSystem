from fastapi import FastAPI
from app.models.base import Base
from app.database.db import engine
import uvicorn

def create_app():
    app = FastAPI(title = "Simple Banking System")
    Base.metadata.create_all(bind=engine)

    return app

app = create_app()

@app.get("/")
def status():
    return {"status": "Ok"}