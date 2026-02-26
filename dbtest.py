from asyncio import run
from database.dao import *
from database.base import create_tables
"""
run(create_tables()) - Создание пустого .sqlite3 файла с пустыми таблицами
run(set_user(tg_id=123, username="ABC")) - Создание записи о польльватели или её обновление
"""
run(create_tables())
run(set_user(tg_id=123, username="ABC"))
