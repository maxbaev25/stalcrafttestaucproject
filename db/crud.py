import datetime
from sqlalchemy.orm import Session
from db.engine import engine
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import ItemHistoryLot
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

async def add_history_lot_async(
        amount: int, time: datetime.datetime,
        price: int) -> None:
    with await AsyncSession(bind=engine) as session:
        session.add(ItemHistoryLot(
            amount=amount, time=time, price=price))
        await session.commit()

async def get_all_history_async():
    with await AsyncSession(bind=engine) as session:
        stmt = select(ItemHistoryLot)
        result = session.execute(stmt)
        history: ItemHistoryLot = result.scalar()
        if not history:
            return None
        return history
            
async def gey_history_by_time_async(time: datetime.datetime):
    with await AsyncSession(bind=engine) as session:
        stmt = select(ItemHistoryLot).where(ItemHistoryLot.time == time)
        result = session.execute(stmt)
        history: ItemHistoryLot = result.scalar()
        if not history:
            return None
        return history
            
async def gey_history_by_amount_async(amount: int):
    with await AsyncSession(bind=engine) as session:
        stmt = select(ItemHistoryLot).where(ItemHistoryLot.amount == amount)
        result = session.execute(stmt)
        history: ItemHistoryLot = result.scalar()
        if not history:
            return None
        return history
