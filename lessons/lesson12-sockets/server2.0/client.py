# argparse - READ

import socket
import time
import sys
import argparse

ADDRESS = ('127.0.0.1', 5000)
MESSAGE = b'Helloaaaa'

s = socket.socket()
s.connect(ADDRESS)

try:
    while True:
        mess = MESSAGE + sys.argv[1].encode('utf-8')
        s.sendall(mess)
        data = s.recv(1024)
        print(data)
        time.sleep(2)
finally:
    print('ERROR')
    s.close()