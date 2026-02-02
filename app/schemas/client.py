from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class ClientBase(BaseModel):
    first_name: str
    last_name: str
    initial_balance: Decimal


class ClientCreate(ClientBase):
    pass


class ClientResponse(ClientBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
