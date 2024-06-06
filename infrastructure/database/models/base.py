from datetime import datetime

from sqlalchemy import DateTime, BigInteger, Column, String, Integer, Date, ForeignKey
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, relationships
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.functions import func
from typing_extensions import Annotated

engine = create_async_engine(url='sqlite+aiosqlite://db.sqlite3')
async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    name = Column(String(100), nullable=False)


class Friend(Base):
    __tablename__ = 'friends'
    id = Column(Integer, primary_key=True,
                user_id=Column(Integer, ForeignKey('users.id'), nullable=False)
    name = Column(String(100), nullable=False)
    birthday = Column(Date, nullable=False)
    user = relationship('User', backref='friends')
