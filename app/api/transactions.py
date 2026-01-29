from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.repositories.transactions import TransactionRepository
from app.schemas.transaction import TransactionResponse, TransactionCreate
from app.services.transactions import TransactionService

router = APIRouter(prefix="/transactions")

@router.post("/", response_model=TransactionResponse)
def create_transaction(data: TransactionCreate, db: Session = Depends(get_db)):
    service = TransactionService(db)
    return service.create_transaction(client_id=data.client_id,
                                        transaction_type=data.transaction_type,
                                        amount=data.amount)
