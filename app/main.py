from fastapi import FastAPI

from app.api.clients import router as clients_router
from app.api.transactions import router as transactions_router
from app.database.db import engine
from app.exception_handlers import register_exception_handlers
from app.models.base import Base


def create_app():
    app = FastAPI(title="Simple Banking System")
    Base.metadata.create_all(bind=engine)

    return app


app = create_app()

Base.metadata.create_all(bind=engine)

register_exception_handlers(app)

app.include_router(clients_router)
app.include_router(transactions_router)


@app.get("/", tags=["Status check"])
def status():
    return {"status": "Ok"}
