from decimal import Decimal
from sqlalchemy.orm import Session
from app.repositories.transactions import TransactionRepository

class TransactionService:

    def __init__(self, db: Session):
        self.repo = TransactionRepository(db)

    def create_transaction(self, client_id: int, transaction_type: str, amount: Decimal):
        return self.repo.create(client_id, transaction_type, amount)

    def list_transactions(self, client_id: int):
        return self.repo.list(client_id)
    
