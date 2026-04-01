from datetime import datetime

from sqlalchemy import Column, Integer, String, \
    BOOLEAN, Text, DateTime
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass

class ItemHistoryLot(Base):
    __tablename__ = 'ItemHistoryLots'
    id = Column(Integer, primary_key=True)
    item = Column(Text)
    region = Column(Text)
    price = Column(Integer)
    amount = Column(Integer)
    time = Column(DateTime)
