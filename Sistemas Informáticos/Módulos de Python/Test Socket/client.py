from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread, Lock
import time

class Client:

    host = 'localhost'
    port = 54321
    bufsize = 512
    addr = (host, port)

    def __init__(self, name):
        self.client_s = socket(AF_INET, SOCK_STREAM)
        self.client_s.connect(self.addr)
        self.messages = []
        receive_thread = Thread(target=self.receive_messages)
        receive_thread.start()
        self.send_message(name)
        self.lock = Lock()

    def receive_messages(self):
        while True:
            try:
                message = self.client_s.recv(self.bufsize).decode()
                self.lock.acquire()
                self.messages.append(message)
                self.lock.release()
                print(message)
            except Exception as e:
                print('[ERROR]', e)
                break

    def send_message(self, message):
        self.client_s.send(bytes(message, 'utf8'))
        if message == '{quit}':
            self.client_s.close()

    def get_messages(self):
        self.lock.acquire()
        self.lock.release()
        return self.messages

    def disconnect(self):
        self.send_message('{quit}')