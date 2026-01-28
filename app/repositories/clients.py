from decimal import Decimal
from sqlalchemy import select
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
    
