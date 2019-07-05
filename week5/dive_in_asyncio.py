import asyncio


# @asyncio.coroutine
# def hello_world():
#     while True:
#         print('Hello, world')
#         yield from asyncio.sleep(1.0)

async def hello_world():
    while True:
        print('Hello, world')
        await asyncio.sleep(1.0)

print(type(hello_world()))

loop = asyncio.get_event_loop()
loop.run_until_complete(hello_world())
loop.close()
