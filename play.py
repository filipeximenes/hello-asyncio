import time
import asyncio


async def coro():
    print('aqui')


async def main(loop):
    # print('registering callbacks')
    # event_loop.call_later(0.2, callback, 1)
    # event_loop.call_later(0.1, callback, 2)
    # event_loop.call_soon(callback, 3)

    # await asyncio.sleep(2)

    print('Done')

event_loop = asyncio.get_event_loop()
try:
    print('entering event loop')
    event_loop.run_until_complete(main(event_loop))
finally:
    print('closing event loop')
    event_loop.close()
