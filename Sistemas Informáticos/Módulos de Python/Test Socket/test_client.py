from client import Client
import time

c1 = Client('Jose')
c2 = Client('Paco')

c2.send_message('Hola, soy Paco')
c2.send_message('¿Qué pasa?')
time.sleep(1)
c1.send_message('Hola, nada')
time.sleep(1)
c2.send_message('Pos vale...')


c1.disconnect()
time.sleep(3)
c2.disconnect()