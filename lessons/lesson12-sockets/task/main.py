import threading
import socket
import collections
import game

ADDRESS = ('127.0.0.1', 5003)

s = socket.socket()
s.bind(ADDRESS)
s.listen(5)

player1 = None

def game_loop(p1, p2):
    field = game.Field()
    players = collections.deque([p1, p2])
    while not field.game_over():
        players[0].sendall((str(field) + '\n\r').encode('utf-8'))
        x, y = players[0].recv(1024).strip().split()
        print('MOVE', x, y)
        field.set_symbol(int(x), int(y), 'X')
        players.rotate()
    player1.close()
    player2.close()


while True:
    c, a = s.accept()
    print('Connected', a)
    if player1 is None:
        player1 = c
        print('PLAYER 1 connected')
    else:
        player2 = c
        t = threading.Thread(target=game_loop, args=(player1, player2))
        t.start()
        player1 = None
