import socket
import ssl
import os
import sys
import colorama # Library for color text output

from server_init import debug_messages # Function for coloring debug messages | customization
from server_init import color_messages # Function to color subsequent messages forever | customization


DEBUG = 1 # The presence of comments inthe output and more detailed work, set at your discretion to control the operation of the program

print('Available customizations:\n 1 - default (white/black)\n 2 - green\n 3 - red\n 4 - blue')

try:
    mode = int(input('Your choice >> '))
    if mode != 1 and mode != 2 and mode != 3 and mode != 4:
        mode = 1
except Exception as e:
    print('Exception:',e)
    mode = 1
    

try:
    init_port = int(sys.argv[1]) # Port for transferring certificates
    port = int(sys.argv[2]) # Messaging port

    if DEBUG == 1:
        debug_messages(mode, '[DEBUG] Initialization with arguments was successful')

except IndexError:
    if DEBUG == 1:
        debug_messages(mode, '[DEBUG] Server initialization due to missing arguments...')

    init_port = int(input('Enter the port for certificate exchange >> '))
    port = int(input('Enter the messaging port >> '))

    if DEBUG == 1:
        debug_messages(mode, '[DEBUG] Initialization with arguments was successful')

if DEBUG == 1:
    debug_messages(mode, '[DEBUG] Running the initialization script for certificate exchange')

os.system(f'python3 server_init.py {init_port} {DEBUG} {mode}')

if DEBUG == 1:
    debug_messages(mode, '[DEBUG] Certificate exchange completed')

client_certificate = 'client.crt'

server_key = 'server.key' 
server_certificate = 'server.crt' 

if DEBUG == 1:
    debug_messages(mode, '[DEBUG] Context initialization')

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH) # Create context
context.load_cert_chain(certfile = server_certificate, keyfile = server_key) # Specify the path to the server certificate and its key
context.load_verify_locations(cafile = client_certificate) # Specify the path to the server certificate
context.verify_mode = ssl.CERT_REQUIRED # Certificate verification | A certificate is required for authentication
context.options |= ssl.OP_SINGLE_ECDH_USE # Key generation
context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1 | ssl.OP_NO_TLSv1_2 # An indication of which versions of the TLS protocol are prohibited from being used when connecting; the old ones have bugs that allow messages to be decrypted; current TLS cersion - 1.3

if DEBUG == 1:
    debug_messages(mode,  'Connection...')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as s: # Socket connection 

    s.bind(('',port))
    s.listen(1)

    with context.wrap_socket(s, server_side = True) as securesock: # Wrapper for secure messaging, encrypts and decrypts message

        print('Version: ', securesock.version())
        conn, addr = securesock.accept()
        print('Address: ',addr)

        if DEBUG == 1:
            debug_messages(mode, '[DEBUG] Connection successfully initialized')

        print(colorama.Style.BRIGHT)
        color_messages(mode)
        while 1:
            try:
                message = conn.recv(1024).decode()

                if not message:
                    if mode != 3:
                        print(colorama.Fore.RED, 'Connection closed by client')
                        break
                    else:
                        print('Connection closed by client')
                        break

                print(f'\n---\nMessage from: {addr}\nMessage: {message}\n---\n')
                message = input('>> ')
                conn.send(message.encode())
                
            except KeyboardInterrupt:
                if mode != 3:
                    print(colorama.Fore.RED, '\nExiting...')
                    break
                else:
                    print('\nExiting')
                    break
        
