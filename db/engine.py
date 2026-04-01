from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from db.models import Base

sqlite_db = "sqlite+aiosqlite:///stalcraft.db"

engine = create_async_engine(url=sqlite_db)

# Base.metadata.create_all(bind=engine)
# async_session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
