from decimal import Decimal
from sqlalchemy.orm import Session
from app.repositories.transactions import TransactionRepository
from app.repositories.clients import ClientRepository
from app.models.client import Client
from app.models.enums.transaction_type import TransactionType
from app.exceptions import NegativeAmountError, InsufficientFundsError, UnknownOperation

class TransactionService:

    def __init__(self, db: Session):
        self.repoTransaction = TransactionRepository(db)
        self.repoClient = ClientRepository(db)

    def create_transaction(self, client_id: int, transaction_type: TransactionType, amount: Decimal):
        if amount < 0:
            raise NegativeAmountError("Amount cannot be negative.")
        
        client = self.repoClient.get(client_id)
        balance_before = client.initial_balance

        if transaction_type == TransactionType.DEPOSIT:
            balance_after = balance_before + amount

        elif transaction_type == TransactionType.WITHDRAWAL:
            if balance_before < amount:
                raise InsufficientFundsError(f"Client {client_id} has insufficient funds")
            balance_after = balance_before - amount
        
        else:
            raise UnknownOperation(f"Unknown transaction type {transaction_type}.")

        client.initial_balance = balance_after

        return self.repoTransaction.create(client_id, transaction_type, amount, balance_after)

    def list_client_transactions(self, client_id: int):
        return self.repoTransaction.list(client_id)
    
    def list_all_transactions(self):
        return self.repoTransaction.list_all()
