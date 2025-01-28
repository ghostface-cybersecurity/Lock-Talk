import socket
import ssl
import sys
import os

try:
    host = sys.argv[1]
    port = int(sys.argv[2])
except IndexError:
    host = input('Enter host >> ')
    port = int(input('Enter port >> '))

os.system(f'python3 init.py {host} 8000')

client_key = 'client.key'
client_certificate = 'client.crt'
server_certificate = 'server.crt'

context = ssl.SSLContext(ssl.PROTOCOL_TLS, cafile = server_certificate) # Create context
context.load_cert_chain(certfile = client_certificate, keyfile = client_key) # Indicate the path to the certificate file
context.load_verify_locations(cafile = server_certificate) # Specifying the path of the other part certificate
context.verify_mode = ssl.CERT_REQUIRED # Certificate verification | A certificate is required for authentication
context.options |= ssl.OP_SINGLE_ECDH_USE # Key generation
context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1 | ssl.OP_NO_TLSv1_2 # It is forbidden to use older versions of the TLS protocol

with socket.create_connection((host, port)) as s: # Socket connection
    with context.wrap_socket(s, server_side = False, server_hostname = host) as securesocket: # Wrapper for secure messaging, encrypts and decrypts message
        print('Version:',securesocket.version())
        print(f'Host: {host}')
        while 1:
            try:
                message = input('>> ')
                securesocket.send(message.encode())
                message = securesocket.recv(1024)
                if not message:
                    print('Connection closed by server')
                    break
                print(f'\n---\nMessage from: {host}\nMessage: {message}\n---\n')
            except KeyboardInterrupt:
                print('\nExiting...')
                break
