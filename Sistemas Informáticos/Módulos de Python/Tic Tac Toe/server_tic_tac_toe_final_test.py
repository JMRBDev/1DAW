import sys
from socket import *

# Global Constants
host = ''
port = 5500
addr = (host, port)
max_connections = 10
bufsize = 1024

# Global Variables
servSocket = socket(AF_INET, SOCK_STREAM)
servSocket.bind(addr)

def clientCommunication():
    messageFromCli = servSocket.recv(bufsize).decode('utf-8')
    
    while True:
        msg = servSocket.recv(bufsize)
        if msg == bytes('{quit}', 'utf-8'):
            servSocket.close()
            print('[CLOSED]')
            break

        else:
            print(msg.decode('utf-8'))

if __name__ == '__main__':
    servSocket.listen(max_connections)
    print('Waiting for connections')

    clientCommunication()