# client-init.py - module for initializing a key and certificate and exchanging them

import os
import socket
import sys
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
    host = sys.argv[1]
    port = int(sys.argv[2])
    DEBUG = int(sys.argv[3])
    mode = int(sys.argv[4])



    if DEBUG == 1:
        debug_messages(mode, '[DEBUG] Now the openssl library command will be launched to create a key and certificate, as well as the command to create a server certificate record file')

    os.system('openssl req -new -newkey rsa:3072 -days 365 -nodes -x509 -keyout client.key -out client.crt') # Command to create key and certificate files

    os.system('touch server.crt')


    if DEBUG == 1:
        debug_messages(mode, '[DEBUG] Transfer and receipt of certificate')

    with socket.create_connection((host,port)) as s: 

        with open('client.crt','rb') as crt_file:
            client_crt = crt_file.read()

        s.sendall(client_crt) # Client certificate submission process
        data = s.recv(4096) # Accepting the server certificate and saving it

        with open('server.crt', 'wb') as crt_file:
            crt_file.write(data)
        
        s.close()

    if DEBUG == 1:
        debug_messages(mode, '[DEBUG] Transfer and receipt of certificates is completed')
if __name__ == '__main__':
    main()