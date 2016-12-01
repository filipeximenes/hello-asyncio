import asyncio


loop = asyncio.get_event_loop()

async def sleep_a_little(t):
    await asyncio.sleep(t)
    print('Done sleeping', t)


async def main_task():
    for i in range(10):
        loop.create_task(sleep_a_little(i/2))
        await asyncio.sleep(0.001)


loop.create_task(main_task())
loop.run_forever()
