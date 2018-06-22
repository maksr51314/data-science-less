import socket
import threading


ADDRESS = ('127.0.0.1', 5000)

s = socket.socket()
s.bind(ADDRESS)
s.listen(5)

def handle(clientSocket):
    while True:
        data = clientSocket.recv(1024)

        if not data:
            clientSocket.close()
            return

        print('DATA', data)
        clientSocket.sendall(data)

while True:
    client, address = s.accept()
    print('Connected', address)
    thread = threading.Thread(target=handle, args=(client,))
    thread.start()




# s.close()