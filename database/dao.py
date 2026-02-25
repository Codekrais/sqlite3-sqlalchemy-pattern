import asyncio
from database.base import connection, create_tables
from database.models import User
from sqlalchemy import select
from typing import List, Dict, Any, Optional
from sqlalchemy.exc import SQLAlchemyError

@connection
async def set_user(session, tg_id: int, username: str, full_name: str = None) -> Optional[User]:
    """
    Принимает chat_id, username, full_name
    Проверяет наличие записи об переданном chat_id:
        если есть, то обновляет данные там,
        если нету, то созадет новую запись
    """
    try:
        user = await session.scalar(select(User).filter_by(id=tg_id))

        if not user:
            new_user = User(id=tg_id, username=username, full_name=full_name)
            session.add(new_user)
            await session.commit()
            print(f"Зарегистрировал пользователя с ID {tg_id}!")
            return None
        else:
            user.username = username
            user.full_name = full_name
            await session.commit()
            print(f"Обновил данные пользователя с ID {tg_id}!")
            return user
    except SQLAlchemyError as e:
        print(f"Ошибка при добавлении пользователя: {e}")
        await session.rollback()

@connection
async def get_ids(session) -> Optional[List]:
    """
    Возвращает список ID
    """
    ids = await session.scalars(select(User.id))
    return list(ids)

@connection
async def get_usernames(session) -> Optional[List]:
    """
    Возвращает список Usernames
    """
    usersnames = await session.scalars(select(User.username))
    return list(usersnames)
