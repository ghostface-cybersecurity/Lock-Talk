# init.py - module for initializing a key and certificate and exchanging them

import socket
import sys
import os

port = int(sys.argv[1])

os.system('openssl req -new -newkey rsa:3072 -days 365 -nodes -x509 -keyout server.key -out server.crt') # command to create key and certificate

os.system('touch client.crt') 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as s:
    s.bind(('',port))
    s.listen(1)
    conn, addr = s.accept()
    print(f'Address: {addr}')
    data = conn.recv(4096) # accepting client certificate and saving it
    with open('client.crt', 'wb') as crt_file:
        crt_file.write(data)
    with open('server.crt', 'rb') as crt_file: # sending the server certificate to the client
        server_crt = crt_file.read()
    conn.send(server_crt)
    conn.close()
