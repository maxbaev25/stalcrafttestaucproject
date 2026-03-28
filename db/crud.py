import datetime
from sqlalchemy.orm import Session
from db.engine import engine
from db.models import ItemHistoryLot

async def add_history_lot(
        amount: int, time: datetime.datetime,
        price: int) -> None:
    with Session(bind=engine) as session:
        session.add(ItemHistoryLot(
            amount=amount, time=time, price=price))
        session.commit()

async def get_all_history():
    with Session(bind=engine) as session:
        stmt = select(ItemHistoryLot)
        result = session.execute(stmt)
        history: ItemHistoryLot = result.scalar()
        if not history:
            return None
        return history

