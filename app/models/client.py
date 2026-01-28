from sqlalchemy import Column, Integer, String, ForeignKey, Float, Numeric
from models.base import Base
class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    initial_balance = Column(Numeric(12,2), default=0.0)
