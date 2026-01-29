from decimal import Decimal
from sqlalchemy import select, delete
from sqlalchemy.orm import Session
from app.models.transaction import Transaction
from app.models.client import Client

class TransactionRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, client_id: int, transaction_type: str, amount: Decimal, balance_after: Decimal):
        transaction = Transaction(client_id = client_id,
                                    transaction_type = transaction_type,
                                    amount = amount,
                                    balance_after = balance_after)
        self.db.add(transaction)
        self.db.commit()
        self.db.refresh(transaction)
        return transaction
    
    def list(self, client_id: int):
        statement = select(Transaction).where(Transaction.client_id == client_id)
        return list(self.db.execute(statement).scalars().all())
    
    def list_all(self):
        statement = select(Transaction)
        return list(self.db.execute(statement).scalars().all())
    