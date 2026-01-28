from decimal import Decimal
from sqlalchemy import select, delete
from sqlalchemy.orm import Session
from app.models.client import Client


class ClientRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, first_name: str, last_name: str, initial_balance: Decimal):
        client = Client(first_name = first_name,
                            last_name = last_name,
                            initial_balance = initial_balance)
        self.db.add(client)
        self.db.commit()
        self.db.refresh(client)
        return client
    
    def get(self, client_id: int):
        statement = select(Client).where(Client.id == client_id)
        return self.db.execute(statement).one_or_none()
    
    def list(self):
        statement = select(Client)
        return list(self.db.execute(statement).all())
    
    def delete(self, client_id: int):
        statement = delete(Client).where(Client.id == client_id)
        result = self.db.execute(statement)
        self.db.commit()
        return result.one_or_none()
    