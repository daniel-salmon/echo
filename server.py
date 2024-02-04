# server.py

from socket import *


def main(args):
    port = parse_args(args)
    server(('0.0.0.0', port))


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


def server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)
    while True:
        client, addr = sock.accept()
        print("Connection from ", addr)
        handler(client, addr)


def handler(client, addr):
    with client:
        while True:
            msg = client.recv(100)
            if not msg:
                break
            client.send(b'echo: ' + msg)
    print(f"Connection from {addr} closed")


if __name__ == '__main__':
    import sys
    main(sys.argv)
