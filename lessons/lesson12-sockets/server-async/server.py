import socket
import select

ADDRESS = ('127.0.0.1', 5000)

s = socket.socket()
s.bind(ADDRESS)
s.setblocking(False)  # do not wait answer
s.listen(5)

connections = [s]


def handle(read_socket):
    data = read_socket.recv(1024)
    if not data:
        connections.remove(read_socket)
        read_socket.close()
        return
    read_socket.sendall(data)


while True:
    read_sockets, a, b = select.select(connections, [], [])

    for read_socket in read_sockets:
        if read_socket == s:
            client = read_socket.accept()
            connections.append(client)
        else:
            handle(read_socket)


            # c, a = s.accept()
            # print('Connected', a)
