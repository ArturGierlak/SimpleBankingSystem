from fastapi import FastAPI
from app.models.base import Base
from app.database.db import engine
import uvicorn
from app.api.clients import router as clients_router
def create_app():
    app = FastAPI(title = "Simple Banking System")
    Base.metadata.create_all(bind=engine)

    return app

app = create_app()

Base.metadata.create_all(bind=engine)

app.include_router(clients_router)
@app.get("/")
def status():
    return {"status": "Ok"}