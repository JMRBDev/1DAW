import sys
from socket import *

# Global Constants
host = 'localhost'
port = 5500
addr = (host, port)
bufsize = 1024

# Global Variables
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.connect(addr)


def recieveMessages():
    while True:
        try:
            msg = clientSocket.recv(bufsize).decode()
        except Exception as e:
            print('[EXCEPTION]', e)
            break

def sendBroadcast():
    while True:
        try:
            clientSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
            clientSocket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
            clientSocket.sendto('This is a test'.encode(), ('255.255.255.255', port))
        except Exception as e:
            print('[EXCEPTION]', e)
            break

if __name__ == '__main__':
    sendBroadcast()