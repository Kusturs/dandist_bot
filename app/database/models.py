import os
from dotenv import load_dotenv

from sqlalchemy import BigInteger, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

load_dotenv()
engine = create_async_engine(url = os.getenv('SQLALCHEMY_URL'))

async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
	pass


class User(Base):
	__tablename__ = 'users'

	id: Mapped[int] = mapped_column(primary_key = True, autoincrement = True, nullable = False)
	tg_id = mapped_column(BigInteger)


class Review(Base):
	__tablename__ = 'reviews'

	id: Mapped[int] = mapped_column(primary_key = True, autoincrement = True, nullable = True)
	tg_id = mapped_column(BigInteger)
	review: Mapped[str] = mapped_column(String(10000))
	mark: Mapped[int] = mapped_column()


async def async_main():
	async with engine.begin() as conn:
		await conn.run_sync(Base.metadata.create_all)
