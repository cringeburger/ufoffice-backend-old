import asyncpg
import os
from typing import Optional
from asyncpg.connection import Connection
from boto.s3.connection import S3Connection


database_url = S3Connection(os.environ['DATABASE_URL'])

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
