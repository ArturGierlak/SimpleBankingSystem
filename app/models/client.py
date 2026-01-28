from sqlalchemy import Column, Integer, String, ForeignKey, Float
from models.base import Base
class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    initial_balance = Column(Float, default=0.0)
