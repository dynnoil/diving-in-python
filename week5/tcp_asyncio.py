import asyncio


async def handle_echo(reader, writer):
    data = await reader.read(1024)
    message = data.decode()
    addr = writer.get_extra_info('peername')
    print('reseived %r from %r' % (message, addr))
    writer.close()

loop = asyncio.get_event_loop()
coro = asyncio.start_server(handle_echo, '127.0.0.1', 10001, loop=loop)
server = loop.run_until_complete(coro)

try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

server.close()
loop.run_until_complete(server.wait_closed())
loop.close()

# connect to server and send message
# import socket
# sock = socket.create_connection(('127.0.0.1', 10001))
# sock.send(b'ping1')


async def tcp_echo_client(message, client_loop):
    _, writer = await asyncio.open_connection('127.0.0.1', 10001, loop=client_loop)

    print('send: %r' % message)
    writer.write(message.encode())
    writer.close()

client_loop = asyncio.get_event_loop()
message = 'hello, world'
loop.run_until_complete(tcp_echo_client(message, loop))
loop.close()
