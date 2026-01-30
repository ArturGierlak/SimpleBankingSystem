from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime, Numeric, func, Enum
from app.models.base import Base
from sqlalchemy.orm import relationship
from app.models.enums.transaction_type import TransactionType

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id"), nullable=False, index=True)
    transaction_type = Column(Enum(TransactionType, name="transaction_type_enum"), nullable=False)
    amount = Column(Numeric(12, 2), nullable=False)
    timestamp = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    balance_after = Column(Numeric(12, 2), nullable=False)

    client = relationship("Client", back_populates="transactions")

    def __str__(self):
        return f"Transaction: Client: {self.client_id}, type: {self.transaction_type},  {self.amount} PLN,, timestamp: {self.timestamp}"
    
    def __repr__(self):
         return f"Transaction (id={self.id}, client={self.client_id}, transaction_type={self.transaction_type}, amount={self.amount}, timestamp={self.timestamp}, balance_after={self.balance_after})"