import socket
import ssl
import os
import sys

try:
    port = int(sys.argv[1])
except IndexError:
    port = int(input('Enter port >> '))

os.system('python3 init.py 8000')

client_certificate = 'client.crt'

server_key = 'server.key' 
server_certificate = 'server.crt' 

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH) # Create context
context.load_cert_chain(certfile = server_certificate, keyfile = server_key) # Indicate the path to the certificate file
context.load_verify_locations(cafile = client_certificate) # Specifying the path of the other part certificate
context.verify_mode = ssl.CERT_REQUIRED # Certificate verification | A certificate is required for authentication
context.options |= ssl.OP_SINGLE_ECDH_USE # Key generation
context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1 | ssl.OP_NO_TLSv1_2 #

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as s: # Socket connection 
    s.bind(('',port))
    s.listen(1)
    with context.wrap_socket(s, server_side = True) as securesock: # Wrapper for secure messaging, encrypts and decrypts message
        print('Version: ', securesock.version())
        conn, addr = securesock.accept()
        print('Address: ',addr)
        while 1:
            try:
                message = conn.recv(1024).decode()
                if not message:
                    print('Connection closed by client')
                    break
                print(f'\n---\nMessage from: {addr}\nMessage: {message}\n---\n')
                message = input('>> ')
                conn.send(message.encode())
            except KeyboardInterrupt:
                print('\nExiting...')
                break
        
