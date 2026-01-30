from decimal import Decimal
from sqlalchemy import select, delete
from sqlalchemy.orm import Session
from app.models.transaction import Transaction
from app.models.client import Client
from app.exceptions import ClientNotFound, InsufficientFundsError
from app.models.enums.transaction_type import TransactionType

class TransactionRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, client_id: int, transaction_type: TransactionType, amount: Decimal, balance_after: Decimal):
        statement = select(Client).where(Client.id == client_id)
        client = self.db.execute(statement).scalars().all()
        if not client:
            raise ClientNotFound(f"Client with id={client_id} does not exist.")
        if balance_after < 0:
            raise InsufficientFundsError(f"Client's id={client_id} funds are not sufficient.")

        transaction = Transaction(client_id = client_id,
                                    transaction_type = transaction_type,
                                    amount = amount,
                                    balance_after = balance_after)
        self.db.add(transaction)
        self.db.commit()
        self.db.refresh(transaction)
        return transaction
    
    def list(self, client_id: int):

        result = self.db.execute(select(Client).where(Client.id == client_id))
        client = result.scalars().first()

        if not client:
            raise ClientNotFound(f"Client with id={client_id} not found.")
        
        statement = select(Transaction).where(Transaction.client_id == client_id)
        return list(self.db.execute(statement).scalars().all())
    
    def list_all(self):
        statement = select(Transaction)
        return list(self.db.execute(statement).scalars().all())
    