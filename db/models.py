from datetime import datetime

from sqlalchemy import Column, Integer, String, \
    BOOLEAN, Text, DateTime
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass

class ItemHistoryLot(Base):
    __tablename__ = 'item_history_lots'
    id = Column(Integer, primary_key=True)
    price = Column(Integer)
    amount = Column(Integer)
    time = Column(DateTime)
