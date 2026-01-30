from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.exceptions import ClientNotFound, ClientAlreadyExists

def register_exception_handlers(app: FastAPI):

    @app.exception_handler(ClientNotFound)
    async def client_not_found_handler(request, exc: ClientNotFound):
        return JSONResponse(status_code=404, content={"error": str(exc)})
    
    @app.exception_handler(ClientAlreadyExists)
    async def client_already_exists_handler(request, exc: ClientAlreadyExists):
        return JSONResponse(status_code=409, content={"error": str(exc)})