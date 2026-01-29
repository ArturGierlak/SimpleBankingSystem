from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel, ConfigDict


class TransactionBase(BaseModel):
    client_id: int
    transaction_type: str
    amount: Decimal

class TransactionCreate(TransactionBase):
    pass

class TransactionResponse(TransactionBase):
    id: int
    timestamp: datetime
    balance_after: Decimal

    class Config():
        model_config = ConfigDict(from_attributes=True)