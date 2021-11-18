import asyncpg
import os
from typing import Optional
from asyncpg.connection import Connection


database_url = os.environ['DATABASE_URL']

class DB:
    conn: Connection = None

    @classmethod
    def get_conn(cls) -> Optional[Connection]:
        if cls.conn is None:
            print('database not found')
        return cls.conn

    @classmethod
    async def connect(cls) -> Optional[Connection]:
        if not cls.conn:
            cls.conn = await asyncpg.connect(database_url)
        return cls.conn

    @classmethod
    async def close(cls) -> None:
        if cls.conn:
            await cls.conn.close()
            cls.conn = None	
