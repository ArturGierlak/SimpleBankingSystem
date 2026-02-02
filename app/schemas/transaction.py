from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel, ConfigDict
from app.models.enums.transaction_type import TransactionType


class TransactionBase(BaseModel):
    client_id: int
    transaction_type: TransactionType
    amount: Decimal

class TransactionCreate(TransactionBase):
    pass

class TransactionResponse(TransactionBase):
    id: int
    timestamp: datetime
    balance_after: Decimal

    model_config = ConfigDict(from_attributes=True)