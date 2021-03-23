# Campeonato de Fórmula 1

class Campeonato:
    temporada = ''
    escuderia = ''
    resultados = []

    def clasificacionPilotos(self, pilotos):
        pilotosOrdenados = sorted(pilotos, key=lambda x: x.puntos, reverse=True)
        position = 1
        for i in pilotosOrdenados:
            print(f'{position}.- {i.nombre} -> {i.puntos}\t\t({i.nacionalidad})')
            position += 1

    def clasificacionEscuderias(self, escuderias):
        puntosEscuderias = {}
        auxPuntosEscuderias = 0
        for i in escuderias:
            for j in i.pilotos:
                auxPuntosEscuderias += j.puntos
            puntosEscuderias[i.nombre] = auxPuntosEscuderias

        escuderiasOrdenadas = sorted(puntosEscuderias.items(), key=lambda kv: kv[1], reverse=True)
        position = 1
        for i in escuderiasOrdenadas:
            print(f'{position}.- {i[0]} -> {i[1]}')
            position += 1

    def mostrarCalendario(self):
        # calendario = [f'Carrera1: España, 10/01/2020 --> Ganador: {piloto1.nombre}', f'Carrera2: Francia, 12/01/2020 --> Ganador: {piloto2.nombre}']
        #print(calendario)
        for i in self.resultados[1::]:
            if 'Posición: 1º' in i:
                print(i)

    def crearResultado(self, nombreCarrera, lugar, fecha, nombrePiloto, posicion):
        self.resultados.append(f'{nombreCarrera}: {lugar}, {fecha} --> {nombrePiloto} Posición: {posicion}º')

    def __init__(self, temporada, escuderia, resultados):
        self.temporada = temporada
        self.escuderia = escuderia
        self.resultados = resultados

class Escuderia:
    nombre = ''
    motor = ''
    pilotos = []

    def __init__(self, nombre, motor, pilotos):
        self.nombre = nombre
        self.motor = motor
        self.pilotos = pilotos

class Piloto:
    nombre = ''
    nacionalidad = ''
    numero = 0
    puntos = 0

    def __init__(self, nombre, nacionalidad, numero, puntos):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.numero = numero
        self.puntos = puntos

class Circuito:
    nombre: ''
    pais: ''
    fecha: ''
    resultado: ''

    def __init__(self, nombre, pais, fecha, resultado):
        self.nombre = nombre
        self.pais = pais
        self.fecha = fecha
        self.resultado = resultado


if __name__ == '__main__':
    piloto1 = Piloto('NombrePiloto1', 'NacionalidadPiloto1', 1, 10)
    piloto2 = Piloto('NombrePiloto2', 'NacionalidadPiloto2', 2, 6)
    escuderia1 = Escuderia('NombreEscuderia1', 'MotorEscuderia1', [piloto1, piloto2])

    piloto3 = Piloto('NombrePiloto3', 'NacionalidadPiloto3', 3, 9)
    piloto4 = Piloto('NombrePiloto4', 'NacionalidadPiloto4', 4, 5)
    escuderia2 = Escuderia('NombreEscuderia2', 'MotorEscuderia2', [piloto3, piloto4])

    circuito1 = Circuito('NombreCircuito1', 'PaisCircuito1', 'FechaCircuito1', piloto1)

    campeonato1 = Campeonato('TemporadaCampeonato1', [escuderia1, escuderia2], [circuito1])

    while True:
        nextAction = input("¿Qué desea hacer? (escuderia, piloto, calendario, añadir): ")
        if nextAction.lower() == 'escuderia':
            campeonato1.clasificacionEscuderias([escuderia1, escuderia2])
        elif nextAction.lower() == 'piloto':
            campeonato1.clasificacionPilotos([piloto1, piloto2, piloto3, piloto4])
        elif nextAction.lower() == 'calendario':
            campeonato1.mostrarCalendario()
        elif nextAction.lower() == 'añadir':
            campeonato1.crearResultado(input("Nombre de la carrera --> "),
                                       input("Lugar --> "),
                                       input("Fecha --> "),
                                       input("Piloto --> "),
                                       input("Posición --> "))
        else:
            print('Error.')
            break