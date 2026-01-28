import datetime
from decimal import Decimal
from pydantic import BaseModel

class ClientBase(BaseModel):
    first_name: str
    last_name: str
    initial_balance: Decimal

class ClientCreate(ClientBase):
    pass

class ClientResponse(ClientBase):
    id: int

    class Config():
        orm_mode = True