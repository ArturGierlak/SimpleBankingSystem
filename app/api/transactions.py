from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.repositories.transactions import TransactionRepository
from app.schemas.transaction import TransactionResponse, TransactionCreate
from app.services.transactions import TransactionService
from app.services.clients import ClientService

router = APIRouter(prefix="/transactions")

@router.post("/", response_model=TransactionResponse)
def create_transaction(data: TransactionCreate, db: Session = Depends(get_db)):
    """Create a deposit or withdrawal transaction for a client.

        Business rules:
        - Amount must be non-negative.
        - Withdrawals require sufficient balance.
        - Transaction type must be supported (DEPOSIT or WITHDRAWAL).

        Args:
            data: Payload with `client_id`, `transaction_type`, and `amount`.
            service: Resolved `TransactionService` via dependency injection.

        Returns:
            TransactionResponse: The created transaction, including server fields
            like `id`, `timestamp`, and `balance_after`.

        Raises:
            HTTPException: 409 if amount is negative; 404 if client not found;
            409 if insufficient funds; 409 if unsupported transaction type.
    """

    service = TransactionService(db)
    return service.create_transaction(client_id=data.client_id,
                                        transaction_type=data.transaction_type,
                                        amount=data.amount)

@router.get("/{client_id}", response_model=list[TransactionResponse])
def list_client_transactions(client_id: int, db: Session = Depends(get_db)):
    """Return all transactions for the specified client.

        Args:
            client_id: Identifier of the client.
            service: Resolved `TransactionService` via dependency injection.

        Returns:
            List[TransactionResponse]: Transactions in unspecified order.

        Raises:
            HTTPException: 404 if the client does not exist.
    """

    service_transaction = TransactionService(db)
    return service_transaction.list_client_transactions(client_id)
    

@router.get("/", response_model=list[TransactionResponse])
def list_all_transactions(db: Session = Depends(get_db)):
    service = TransactionService(db)
    return service.list_all_transactions()
