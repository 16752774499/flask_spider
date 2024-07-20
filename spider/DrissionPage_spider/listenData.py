import asyncio

from RedisMQ import RedisMQ
from Spinner import Spinner


# 轮询监听
async def listenData():
    mq = RedisMQ(host='192.168.0.6', port=6379, db=3, password='redis_QBc2mF')
    await mq.init()
    s = Spinner('listen')
    s.start()
    while True:

        data = await mq.consumer()
        if data is not None:
            s.stop()
            print(data)
            """
                进行出库后的相关处理
            """
        else:
            s.start()
            continue


# 确定有数据异步弹出
async def pop_tasks(size: int):
    redisClient = RedisMQ(host='192.168.0.6', port=6379, db=3, password='redis_QBc2mF')
    await redisClient.init()
    tasks = [
        asyncio.create_task(redisClient.consumer()) for _ in range(size)
    ]
    await asyncio.gather(*tasks)
    await redisClient.close()


if __name__ == '__main__':
    asyncio.run(listenData())
