#!/usr/bin/python3 

import socket
from time import gmtime, strftime

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 8080))
serversocket.listen(5)

while True:
    connection, address = serversocket.accept()
    connection.send('CN'.encode())
    buf = connection.recv(2)
    cmd =  buf.decode('utf-8')
    if len(buf) > 0:
        print('['+strftime("%Y-%m-%d %H:%M:%S", gmtime())+'] '+'Command '+cmd+' has been received', flush=True)
        connection.send('CM'.encode())
        if cmd == 'EN':
            break
    

print("Process finished!", flush=True)
