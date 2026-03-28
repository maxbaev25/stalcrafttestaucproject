import datetime
from sqlalchemy.orm import Session
from db.engine import engine
from db.models import ItemHistoryLot

async def add_history_lot_async(
        amount: int, time: datetime.datetime,
        price: int) -> None:
    with Session(bind=engine) as session:
        session.add(ItemHistoryLot(
            amount=amount, time=time, price=price))
        session.commit()

async def get_all_history_async():
    with Session(bind=engine) as session:
        stmt = select(ItemHistoryLot)
        result = session.execute(stmt)
        history: ItemHistoryLot = result.scalar()
        if not history:
            return None
        return history
            
async def gey_history_by_time_async(time: datetime.datetime):
    with Session(bind=engine) as session:
        stmt = select(ItemHistoryLot).where(ItemHistoryLot.time == time)
        result = session.execute(stmt)
        history: ItemHistoryLot = result.scalar()
        if not history:
            return None
        return history
            
async def gey_history_by_amount_async(amount: int):
    with Session(bind=engine) as session:
        stmt = select(ItemHistoryLot).where(ItemHistoryLot.amount == amount)
        result = session.execute(stmt)
        history: ItemHistoryLot = result.scalar()
        if not history:
            return None
        return history
