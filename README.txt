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
Current version: 1.9
Languages: Python 3.12.7
Tested on: Kali linux 2024.4 on Kernel Linux 6.11.2 | Windows
Author: ghostface-cybersecurity
Dependencies: OpenSSL 3.4.0
________________________________________________________________________________
                                 DOCUMENTATION
________________________________________________________________________________
Lock-Talk is a console messenger based on TCP sockets and the TLS protocol for 
encrypting messages. 

There is no need to transfer certificates to each other; 
the client and server will generate them and do it for you. 

All you have to do is indicate the information in the certificates, 
wait and start communicating :)

-------------------------------------------------------------------------------
Now the *_init.py files are needed not only for passing certificates, but also 
for message coloring, since they contain methods to implement this idea. 
Their code has also been changed for greater cleanliness and stability. 
After receiving the certificates, the client and server establish a shared 
key and encrypt messages based on the Diffie-Hellman algorithm. 
The dialogue will continue until the client or server is disabled using 
the ctrl+C command.

Also, the init.py files create a key and certificate using the openssl library.

--------------------------------------------------------------------------------
                                    LAUNCH
--------------------------------------------------------------------------------
// Server lauch

// You need to specify an argument: through which port the server will 
// communicate with the client. If you do not specify it, you will 
// be prompted for a port automatically upon startup.

python3 server.py <Port for transferring certificates> <Messaging port>
// or
python3 server.py

// Then he will ask you for information to obtain a certificate. Enter as you wish.

// You will then be presented with a blank line where you can enter something, 
// but it will not respond. This is the client's expectation.

// -----------------------------

// Client connection

// When running, you need to specify the arguments: Host and port. 
//If you do not specify them, the program will request them from you automatically.

python3 client.py <Host> <Port for transferring certificates> <Messaging port>
// or
python3 client.py


// Then he will ask you for information to obtain a certificate. Enter as you wish.

// Now they will exchange certificates, connect to each other and you can 
//start your hidden communication.

________________________________________________________________________________
                                     UPDATES
________________________________________________________________________________
1. Now the *_init.py files are needed not only for passing certificates, but also 
   for message coloring, since they contain methods to implement this idea.
2. Added customization.
3. The code has become more readable.
4. A debugger has been added that allows you to view information about the 
   initialization process, as well as the ability to customize it.
5. The names of the initialization scripts, as well as their code, 
   have been changed for greater cleanliness and stability.
6. Added customization implementation for Windows OS.
7. Documentation changes.

________________________________________________________________________________
                                  LEGAL STATEMENT
________________________________________________________________________________
By downloading, modifying, redistributing, and/or executing Lock-Talk, the
user agrees to the contained LEGAL.txt statement found in this repository.

I, ghostface-cybersecurity, the creator, take no legal responsibility for unlawful actions
caused/stemming from this program. 

Use responsibly and ethically!