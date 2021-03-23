import datetime
from agencia import *

if __name__ == "__main__":
    e1 = Evento("Concierto de Sphinx",datetime.date.today(),Ciudad("Sevilla",200,60.35),1,34)
    e2 = Evento("La vida de Brian",datetime.date.today(),Ciudad("Cádiz",0,52.12),1,7)
    eventos = []
    eventos.append(e1)
    eventos.append(e2)

    agencia = Agencia("Agencia de eventos Gaditana", [e1,e2])
    viaje = Viaje(2,e1,68)

    print(f"----- EVENTOS DE {agencia.nombre.upper()} -----")
    for evento in eventos:
        print(evento)

    while True:
        buscarEvento = input("\nEvento: ")
        if buscarEvento.lower() == "fin":
            print("\n¡Hasta la próxima!")
            exit()
        else:
            for evento in eventos:
                if buscarEvento == evento.denominacion:
                    numeroAsistentes = int(input("Asistentes: "))
                    precioTotal = evento.precioPersona(evento.fecha, numeroAsistentes)
                    print("Precio total:", str(round(precioTotal, 2)) + "€")