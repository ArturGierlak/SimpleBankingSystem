import datetime
from decimal import Decimal
from pydantic import BaseModel


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
        orm_mode = True