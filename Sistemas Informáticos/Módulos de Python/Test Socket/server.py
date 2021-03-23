from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import datetime
from user import User

# Global constants
host = 'localhost'
port = 54321
addr = (host, port)
max_connections = 10
bufsize = 512

# Global variables
users = []

server_s = socket(AF_INET, SOCK_STREAM)
server_s.bind(addr)

def broadcast(message, name):
    for user in users:
        client = user.client
        client.send(bytes(name, 'utf8') + message)

def client_communication(user):
    client = user.client
    
    # Get username
    name = client.recv(bufsize).decode('utf8')
    user.set_name(name)
    message = bytes(f'{name} has joined the chat room', 'utf8')
    broadcast(message, '')

    while True:
        try:
            message = client.recv(bufsize)
            if message == bytes('{quit}', 'utf8'):
                client.close()
                users.remove(user)
                broadcast(f'{name} has left the chat room...', '')
                print(f'[DISCONNECTED] {name} disconnected')
                break
            else:
                broadcast(message, name + ": ")
                print(f'{name}: ' + message.decode('utf8'))
        except Exception as e:
            print('[ERROR]', e)
            break

def wait_for_connection():
    run = True
    while run:
        try:
            client, addr = server_s.accept()
            user = User(addr, client)
            users.append(user)
            print(f'[CONNECTION] {addr} connected to the server at {datetime.datetime.now().hour}:{datetime.datetime.now().minute}:{datetime.datetime.now().second}')
            Thread(target=client_communication, args=(user,)).start()
        except Exception as e:
            print('[ERROR]', e)
            run = False

    print('SERVER CRASHED')

if __name__ == '__main__':
    server_s.listen(max_connections)
    print('[STARTED] Server is waiting for connections...')
    accept_thread = Thread(target=wait_for_connection)
    accept_thread.start()
    accept_thread.join()
    server_s.close()