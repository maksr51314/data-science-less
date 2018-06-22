import socket

ADDRESS = ('127.0.0.1', 5000)
MESSAGE = b'Hello'

s = socket.socket()
s.connect(ADDRESS)
s.sendall(MESSAGE)

data = s.recv(1024)
print(data)
s.close()