 ####      #####     ####   ###  ##           ######     ##     ####     ###  ##
  ##      ##   ##   ##  ##   ##  ##           # ## #    ####     ##       ##  ##
  ##      ##   ##  ##        ## ##              ##     ##  ##    ##       ## ##
  ##      ##   ##  ##        ####               ##     ##  ##    ##       ####
  ##   #  ##   ##  ##        ## ##              ##     ######    ##   #   ## ##
  ##  ##  ##   ##   ##  ##   ##  ##             ##     ##  ##    ##  ##   ##  ##
 #######   #####     ####   ###  ##            ####    ##  ##   #######  ###  ##

________________________________________________________________________________
                                     ABOUT
________________________________________________________________________________
Description: Console messenger between client and server using TLS 1.3 
             protocol to encrypt messages 
Program: Lock-Talk | Console messanger
Current version: 1.2
Languages: Python 3.12.7
Tested on: Kali linux 2024.4 on Kernel Linux 6.11.2
Author: ghostface-cybersecurity

________________________________________________________________________________
                                 DOCUMENTATION
________________________________________________________________________________
Lock - Talk is a console messenger based on TCP sockets and the TLS protocol for 
encrypting messages. 

There is no need to transfer certificates to each other; 
the client and server will generate them and do it for you. 

All you have to do is indicate the information in the certificates, 
wait and start communicating :)

-------------------------------------------------------------------------------
The init.py files are only needed at the very beginning to transfer certificates 
to each other. Then the client and server set a shared key and encrypt messages 
based on the Diffie-Hellman algorithm. The dialogue will continue until the 
client or server disconnects using the command ctrl+C.

Also, the init.py files create a key and certificate using the openssl library.

-------------------------------------------------------------------------------
                                    LAUNCH
-------------------------------------------------------------------------------
// Server lauch

// You need to specify an argument: through which port the server will 
// communicate with the client. If you do not specify it, you will 
// be prompted for a port automatically upon startup.

python3 server.py 8080
// or
python3 server.py

// Then he will ask you for information to obtain a license. Enter as you wish.

// You will then be presented with a blank line where you can enter something, 
// but it will not respond. This is the client's expectation.

// -----------------------------

// Client connection

// When running, you need to specify the arguments: Host and port. 
//If you do not specify them, the program will request them from you automatically.

python3 client.py
// or
python3 client.py 192.168.1.101 8080

// Then he will ask you for information to obtain a license. Enter as you wish.

// Now they will exchange certificates, connect to each other and you can 
//start your hidden communication.

______________________________________________________________________________
                                     TO-DO
______________________________________________________________________________
1. In the plan: add to the next version of Lock-Talk an indication of the port 
   for exchanging certificates. Add changes to documentation. [X] 
   | Looking forward to this in future versions |

______________________________________________________________________________
                                  LEGAL STATEMENT
______________________________________________________________________________
By downloading, modifying, redistributing, and/or executing Lock-Talk, the
user agrees to the contained LEGAL.txt statement found in this repository.

I, ghostface-cybersecurity, the creator, take no legal responsibility for unlawful actions
caused/stemming from this program. 

Use responsibly and ethically!
