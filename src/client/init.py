# init.py - module for initializing a key and certificate and exchanging them

import os
import socket
import sys

host = sys.argv[1]
port = int(sys.argv[2])

os.system('openssl req -new -newkey rsa:3072 -days 365 -nodes -x509 -keyout client.key -out client.crt') # # command to create key and certificate

os.system('touch server.crt')

with socket.create_connection((host,port)) as s: 
    with open('client.crt','rb') as crt_file:
        client_crt = crt_file.read()
    s.sendall(client_crt) # client certificate submission process
    data = s.recv(4096) # accepting the server certificate and saving it
    with open('server.crt', 'wb') as crt_file:
        crt_file.write(data)
    s.close()
