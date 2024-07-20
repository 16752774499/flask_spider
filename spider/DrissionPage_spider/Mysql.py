import asyncio

import aiomysql


class Mysql:
    def __init__(self, host: str = '192.168.0.6', port: int = 3306, user: str = 'spider', password: str = 'spider',
                 db: str = 'spider'):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.conn = None
        self.cur = None

    async def init(self) -> object:
        try:
            self.conn = await aiomysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                db=self.db
            )
            self.cur = await self.conn.cursor()
            print("MySQL 连接成功")
            return self.cur
        except Exception as e:
            print(f"Failed to connect to MySQL: {e}")
            raise

    async def close(self):
        if self.cur:
            try:
                await self.cur.close()
            except Exception as e:
                print(f"Failed to close cursor: {e}")
        if self.conn:
            try:
                self.conn.close()
                await self.conn.wait_closed()
            except Exception as e:
                print(f"Failed to close connection: {e}")
        print("MySQL 连接已关闭")


async def run():
    mysql = Mysql(host='192.168.0.6', port=3306, user='test', password='0987654321', db='test')
    await mysql.init()

    ret = await mysql.cur.execute("select * from test")

    print(ret)

    await mysql.close()


if __name__ == '__main__':
    asyncio.run(run())
