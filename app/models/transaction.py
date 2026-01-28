from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime, Numeric, func
from models.base import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id"), nullable=False, index=True)
    transaction_type = Column(String, nullable=False)
    amount = Column(Numeric(12, 2), nullable=False)
    timestamp = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    balance_after = Column(Numeric(12, 2), nullable=False)
