from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

ASYNC_DB_URL = "mysql+aiomysql://root@db:3306/demo?charset=utf8"

async_engine = create_async_engine(ASYNC_DB_URL, echo=True)
async_session = sessionmaker(
  autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession
)

db_session = sessionmaker(autocommit=False, autoflush=False, bind=async_engine)

Base = declarative_base()

async def get_db():
  async with async_engine() as session:
    yield session
