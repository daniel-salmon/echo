# aserver.py

import asyncio
from socket import *


def main(args):
    port = parse_args(args)
    asyncio.run(server(('localhost', port)))


def parse_args(args):
    if len(args) > 2:
        print("Usage: server.py [port]")
        raise RuntimeError()
    port = 8080
    if len(args) > 1:
        try:
            port = int(args[1])
        except ValueError as e:
            print("port must be an integer")
            raise ValueError()
    return port


async def server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)
    sock.setblocking(False)

    loop = asyncio.get_event_loop()

    while True:
        client, addr = await loop.sock_accept(sock)
        print("Connection from ", addr)
        loop.create_task(handler(client, addr))


async def handler(client, addr):
    loop = asyncio.get_event_loop()
    with client:
        while True:
            msg = await loop.sock_recv(client, 100)
            if not msg:
                break
            await loop.sock_sendall(client, b'echo: ' + msg)
    print(f"Connection from {addr} closed")


if __name__ == '__main__':
    import sys
    main(sys.argv)
