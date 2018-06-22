import socket

ADDRESS = ('127.0.0.1', 5000)

server = socket.socket()
server.bind(ADDRESS)
server.listen(5)

print('WAITING for connections')
client, address = server.accept()
print('Connected', address, client)

data = client.recv(1024)
print('DATA', data)
client.sendall(data)
client.close()
server.close()