from sqlalchemy import func
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine, AsyncSession
from sqlalchemy import BigInteger, Integer, Text, ForeignKey, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from database.settings import url

engine = create_async_engine(url=url)
async_session = async_sessionmaker(engine, class_=AsyncSession)


class Base(AsyncAttrs, DeclarativeBase):
    """
    Базовый родительский класс для последующих моделей
    Наследованный от DeclarativeBase
    """

    pass
