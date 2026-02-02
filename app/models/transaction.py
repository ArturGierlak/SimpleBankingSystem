from sqlalchemy import (
    Column,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    Numeric,
    func,
)
from sqlalchemy.orm import relationship

from app.models.base import Base
from app.models.enums.transaction_type import TransactionType


class Transaction(Base):
    """Database model representing a financial transaction made by a client.

    Each transaction records the operation type (deposit or withdrawal),
    the affected client, the amount processed, and the resulting balance after the transaction
    which is calculated based on client's balance and amount.
    Timestamps are automatically generated on insertion.
    """  # noqa: E501

    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id"), nullable=False, index=True)
    transaction_type = Column(
        Enum(TransactionType, name="transaction_type_enum"), nullable=False
    )
    amount = Column(Numeric(12, 2), nullable=False)
    timestamp = Column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    balance_after = Column(Numeric(12, 2), nullable=False)

    client = relationship("Client", back_populates="transactions")

    def __str__(self):
        return f"Transaction: Client: {self.client_id}, type: {self.transaction_type},  {self.amount} PLN,, timestamp: {self.timestamp}"  # noqa: E501

    def __repr__(self):
        return f"Transaction (id={self.id}, client={self.client_id}, transaction_type={self.transaction_type}, amount={self.amount}, timestamp={self.timestamp}, balance_after={self.balance_after})"  # noqa: E501
