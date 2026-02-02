from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.schemas.client import ClientCreate, ClientResponse
from app.services.clients import ClientService

router = APIRouter(prefix="/clients", tags=["Clients"])


@router.post("/", response_model=ClientResponse)
def create_client(data: ClientCreate, db: Session = Depends(get_db)):
    service = ClientService(db)
    return service.create_client(
        first_name=data.first_name,
        last_name=data.last_name,
        initial_balance=data.initial_balance,
    )


@router.get("/{client_id}", response_model=ClientResponse)
def get_client(client_id: int, db: Session = Depends(get_db)):
    service = ClientService(db)
    return service.get_client(client_id=client_id)


@router.get("/", response_model=list[ClientResponse])
def list_clients(db: Session = Depends(get_db)):
    service = ClientService(db)
    return service.list_clients()


@router.delete("/{client_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_client(client_id: int, db: Session = Depends(get_db)):
    service = ClientService(db)
    return service.delete_client(client_id=client_id)
