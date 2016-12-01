import asyncio


loop = asyncio.get_event_loop()


async def sleep_a_little(t):
    await asyncio.sleep(t)
    print('Done sleeping', t)


async def wrapper():
    for i in range(10):
        await sleep_a_little(i/10)
    return 42


async def main_task():
    r = await wrapper()
    print('response:', r)


loop.run_until_complete(main_task())
