from sqlalchemy.sql.coercions import name
from database.database import async_session, engine, Base


def connection(func):
    """
    Декортаор
    Используется для открытия и закрытия асинхронной сессии базы данных
    """
    async def wrapper(*args, **kwargs):
        async with async_session() as session:
            return await func(session, *args, **kwargs)


    return wrapper


async def create_tables():
    """
    Асинхронное созадние таблицы
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
