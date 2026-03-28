import datetime
from sqlalchemy.orm import Session
from db.engine import engine
from db.models import ItemHistoryLot

async def add_history_lot(
        amount: int, time: str,
        price: int) -> None:
    with Session(bind=engine) as session:
        session.add(StalcraftHistoryTable(
            amount=amount, time=time, price=price))
        session.commit()
