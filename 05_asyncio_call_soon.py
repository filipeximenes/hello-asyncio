import asyncio


def callback(arg):
    print('callback {} invoked'.format(arg))


async def main(loop):
    print('registering callbacks')
    event_loop.call_soon(callback, 1)
    event_loop.call_soon(callback, 2)

    await asyncio.sleep(0.1)


event_loop = asyncio.get_event_loop()
try:
    print('entering event loop')
    event_loop.run_until_complete(main(event_loop))
finally:
    print('closing event loop')
    event_loop.close()
