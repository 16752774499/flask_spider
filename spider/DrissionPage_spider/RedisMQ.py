import json

import aioredis


class RedisMQ:
    def __init__(self, host: str = '192.168.0.6', port: int = 6379, db: int = 9, password: str = None):
        self.queue_name = 'boss_queue'
        self.redisSession = None
        self.host = host
        self.port = port
        self.db = db
        self.password = password

    async def init(self):
        redis_uri = f'redis://{self.host}:{self.port}'
        try:
            self.redisSession = await aioredis.create_redis(
                address=redis_uri,
                db=self.db,
                password=self.password
            )
            print("Redis 连接成功")
        except aioredis.RedisError as e:
            print("Redis 连接失败", e)

    # 入列
    async def producer(self, dataDict: dict):
        await self.redisSession.lpush(self.queue_name, json.dumps(dataDict))
        print(f"入列成功：{dataDict}")
        return None

    # 出列
    async def consumer(self):

        message = await self.redisSession.brpop(self.queue_name, timeout=1)
        if message:
            print(f"出列成功： {message[1].decode('utf-8')}")
            return message[1].decode('utf-8')

    async def close(self):
        if self.redisSession:
            self.redisSession.close()
            await self.redisSession.wait_closed()
            print("Redis 连接已关闭")
