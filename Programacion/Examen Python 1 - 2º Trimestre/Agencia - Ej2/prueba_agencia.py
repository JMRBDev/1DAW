import datetime
from agencia import *

if __name__ == "__main__":
    e1 = Evento("Concierto de Sphinx",datetime.date.today(),Ciudad("Sevilla",200,60.35),1,34)
    e2 = Evento("La vida de Brian",datetime.date.today(),Ciudad("Cádiz",0,52.12),1,7)
    agencia = Agencia("Eventos Alberti", [e1,e2])
    viaje = Viaje(2,e1,68)
    print(agencia)
    print(viaje)