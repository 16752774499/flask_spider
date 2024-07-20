import asyncio

from RedisMQ import RedisMQ
from WebBot import WebBot


async def main():
    redisClient = RedisMQ(host='192.168.0.6', port=6379, db=3, password='redis_QBc2mF')
    await redisClient.init()
    webBot = WebBot(query="Java", city="100010000", nums=10)
    webBot.cleanseData(webBot.listenApi())

    push_tasks = [
        asyncio.create_task(redisClient.producer(res)) for res in webBot.DATA
    ]
    await asyncio.gather(*push_tasks)

    del webBot
    await redisClient.close()


asyncio.run(main())
