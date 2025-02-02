# server-init.py - module for initializing a key and certificate and exchanging them

import socket
import sys
import os
import colorama

def debug_messages(mode: int,text: str):
    if mode == 1:
        print(text)
    elif mode == 2:
        print(colorama.Fore.GREEN, text)
    elif mode == 3:
        print(colorama.Fore.RED, text)
    elif mode == 4:
        print(colorama.Fore.BLUE, text)

    print(colorama.Style.RESET_ALL)

def color_messages(mode: int):
    if mode == 1:
        print()
    elif mode == 2:
        print(colorama.Fore.GREEN)
    elif mode == 3:
        print(colorama.Fore.RED)
    elif mode == 4:
        print(colorama.Fore.BLUE) 

def main():
    port = int(sys.argv[1])
    DEBUG = int(sys.argv[2])
    mode = int(sys.argv[3])

    if DEBUG == 1:
        debug_messages(mode,  '[DEBUG] Now the openssl library command will be launched to create a key and certificate, as well as the command to create a client certificate record file')

    os.system('openssl req -new -newkey rsa:3072 -days 365 -nodes -x509 -keyout server.key -out server.crt') # command to create key and certificate

    os.system('touch client.crt') 

    if DEBUG == 1:
        debug_messages(mode,'[DEBUG] Transfer and receipt of certificate')

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as s:
    
        s.bind(('',port))
        s.listen(1)
        conn, addr = s.accept()
        print(f'Address: {addr}')
        data = conn.recv(4096) # Accepting client certificate and saving it

        with open('client.crt', 'wb') as crt_file:
            crt_file.write(data)

        with open('server.crt', 'rb') as crt_file: # Sending the server certificate to the client
            server_crt = crt_file.read()

        conn.send(server_crt)
        conn.close()

    if DEBUG == 1:
        debug_messages(mode, '[DEBUG] Transfer and receipt of certificates is completed')

if __name__ == '__main__':
    main()