import socket
import ssl
import sys
import os
import colorama # Library for color text output

from client_init import debug_messages # Function for coloring debug messages | customization
from client_init import color_messages # Function to color subsequent messages forever | customization

colorama.init(autoreset = True)

DEBUG = 1 # The presence of comments inthe output and more detailed work, set at your discretion to control the operation of the program

print('Available customizations:\n 1 - default (white/black)\n 2 - green\n 3 - red\n 4 - blue')

try:
    mode = int(input('Your choice >> '))
    if mode != 1 and mode != 2 and mode != 3 and mode != 4:
        mode = 1
except Exception as e:
    print(e)
    mode = 1

try:
    host = sys.argv[1] # Host for communicating with the server
    init_port = int(sys.argv[2]) # Port for transferring certificates
    port = int(sys.argv[3]) # Port for communicating with the server

    if DEBUG == 1:
        debug_messages(mode, '[DEBUG] Initialization with arguments was successful')

except IndexError:

    if DEBUG == 1:
        debug_messages(mode, '[DEBUG] Client initialization due to missing arguments...')

    host = input('Enter server host >> ')
    init_port = int(input('Enter the port for certificate exchange >> '))
    port = int(input('Enter the port to communicate with the server (messaging) >> '))

    if DEBUG == 1:
        debug_messages(mode, '[DEBUG] Initialization with arguments was successful')


if DEBUG == 1:
    debug_messages(mode, '[DEBUG] Running the initialization script for certificate exchange')

os.system(f'python3 client_init.py {host} {init_port} {DEBUG} {mode}')

if DEBUG == 1:
    debug_messages(mode, '[DEBUG] Certificate exchange completed')

server_certificate = 'server.crt'

client_key = 'client.key'
client_certificate = 'client.crt'

if DEBUG == 1:
    debug_messages(mode, '[DEBUG] Context initialization')

context = ssl.SSLContext(ssl.PROTOCOL_TLS, cafile = server_certificate) # Create context
context.load_cert_chain(certfile = client_certificate, keyfile = client_key) # Specify the path to the client certificate and its key
context.load_verify_locations(cafile = server_certificate) # Specify the path to the server certificate
context.verify_mode = ssl.CERT_REQUIRED # Certificate verification | A certificate is required for authentication
context.options |= ssl.OP_SINGLE_ECDH_USE # Key generation
context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1 | ssl.OP_NO_TLSv1_2 # An indication of which versions of the TLS protocol are prohibited from being used when connecting; the old ones have bugs that allow messages to be decrypted; current TLS cersion - 1.3

if DEBUG == 1:
    debug_messages(mode, 'Connection...')

with socket.create_connection((host, port)) as s: # Socket connection

    with context.wrap_socket(s, server_side = False, server_hostname = host) as securesocket: # Wrapper for secure messaging, encrypts and decrypts message

        print('Version:',securesocket.version())
        print(f'Host: {host}')

        if DEBUG == 1:
            debug_messages(mode, '[DEBUG] Connection successfully initialized')

        print(colorama.Style.BRIGHT)
        color_messages(mode)
        while 1:
            try:
                message = input('>> ')
                securesocket.send(message.encode())
                message = securesocket.recv(1024)

                if not message:
                    if mode != 3:
                        print(colorama.Fore.RED, 'Connection closed by server')
                        break
                    else:
                        print('Connection closed by server')

                print(f'\n---\nMessage from: {host}\nMessage: {message}\n---\n')

            except KeyboardInterrupt:
                if mode != 3:
                    print(colorama.Fore.RED, '\nExiting...')
                    break
                else: 
                    print('\nExiting...')
                    break
