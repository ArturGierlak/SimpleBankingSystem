from decimal import Decimal
from sqlalchemy import select, delete
from sqlalchemy.orm import Session
from app.models.client import Client
from app.exceptions import ClientNotFound, ClientAlreadyExists, InsufficientFundsError, NegativeInitialBalance


class ClientRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, first_name: str, last_name: str, initial_balance: Decimal):
        client = Client(first_name = first_name,
                            last_name = last_name)
        client.initial_balance = initial_balance

        if initial_balance < 0:
            raise NegativeInitialBalance(f"Initial balance cannot be negative.")
        
        result = self.db.execute(select(Client).where(Client.last_name == last_name and Client.first_name == first_name)).scalars().first()
        if result:
            raise ClientAlreadyExists(f"Client {first_name} {last_name} already exists in database.")

        self.db.add(client)
        self.db.commit()
        self.db.refresh(client)
        return client
    
    def get(self, client_id: int):
        result = self.db.execute(select(Client).where(Client.id == client_id))
        client = result.scalars().first()

        if not client:
            raise ClientNotFound(f"Client with id={client_id} not found.")
        
        return client
    
    def list(self):
        statement = select(Client)
        return list(self.db.execute(statement).scalars().all())
    
    def delete(self, client_id: int):
        result = self.db.execute(select(Client).where(Client.id == client_id))
        client = result.scalars().first()

        if not client:
            raise ClientNotFound(f"Client with id={client_id} does not exist.")
        
        statement = delete(Client).where(Client.id == client_id)
        result = self.db.execute(statement)
        self.db.commit()
        return result.rowcount > 0
    