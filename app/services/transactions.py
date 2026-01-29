from decimal import Decimal
from sqlalchemy.orm import Session
from app.repositories.transactions import TransactionRepository
from app.repositories.clients import ClientRepository
from app.models.client import Client

class TransactionService:

    def __init__(self, db: Session):
        self.repoTransaction = TransactionRepository(db)
        self.repoClient = ClientRepository(db)

    def create_transaction(self, client_id: int, transaction_type: str, amount: Decimal):
        client = self.repoClient.get(client_id)
        balance_before = client.initial_balance
        balance_after = balance_before + amount
        client.initial_balance = balance_after

        return self.repoTransaction.create(client_id, transaction_type, amount, balance_after)


    
