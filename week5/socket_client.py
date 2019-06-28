import socket

# sock = socket.create_connection(("127.0.0.1", 10001))
# sock.sendall(b"ping".encode("utf8"))
# sock.close()

with socket.create_connection(('127.0.0.1', 10001)) as sock:
    sock.sendall('ping'.encode('utf8'))
