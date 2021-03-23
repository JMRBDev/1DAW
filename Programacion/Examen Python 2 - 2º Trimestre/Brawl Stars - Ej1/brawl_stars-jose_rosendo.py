        # Jose Rosendo

import random
from pathlib import Path
import time

class Jugador:
    nombre = str
    personajes = list

    def __init__(self, nombre):
        self.nombre = nombre

    def crearArchivo(self):
        if not Path(self.nombre).is_file():
            print("El jugador", self.nombre, "no existe. Creando jugador...\n")
            time.sleep(1.2)
            with open(self.nombre, "w") as f:
                return False
        else:
            with open(self.nombre, "r") as f:
                print(f.read())
                return True

    def abrirCaja(self, dias):
        personajes = self.getPersonajes()
        personajes["monedas"] = "monedas"
        poseePersonajes = self.personajes()

        for dia in range(1, int(dias) + 1):
            for caja in range(2):
                print("\nDia", dia, "- Caja normal", caja)
                time.sleep(0.5)
                obtiene = random.choices(list(personajes.values()), [2.7312, 2.7312, 2.7312,
                                                                    1.2096, 1.2096, 1.2096, 1.2096,
                                                                    0.5472, 0.5472, 0.5472,
                                                                    0.2496, 0.2496, 0.2496,
                                                                    0.0624, 0.0624, 0.0624,
                                                                    60])
                if obtiene[0].lower() == "monedas":
                    print("Obtiene:", obtiene[0].capitalize())
                else:
                    posibles = []
                    for personaje, categoria in personajes.items():
                        if categoria == obtiene[0] and personaje not in posibles and obtiene[0].lower() not in poseePersonajes:
                            posibles.append(personaje)

                    repetir = True
                    repeticiones = 0
                    while repetir:
                        obtiene = random.choice(posibles)
                        if obtiene not in poseePersonajes:
                            poseePersonajes.append(obtiene.lower())
                            print("Obtiene:", obtiene.capitalize())
                            time.sleep(0.7)
                            self.setPersonajes(personajes[obtiene], obtiene)
                            repetir = False
                        else:
                            repetir = True

                        repeticiones += 1
                        if repeticiones > len(posibles):
                            print("Obtiene: Monedas\n")
                            time.sleep(0.7)
                            repetir = False

            if list(str(dia))[-1] in ["0", "2", "5", "7"]:
                print("\nDia", dia, "- Caja grande")
                time.sleep(0.5)
                for caja in range(3):
                    obtiene = random.choices(list(personajes.values()), [2.7312, 2.7312, 2.7312,
                                                                        1.2096, 1.2096, 1.2096, 1.2096,
                                                                        0.5472, 0.5472, 0.5472,
                                                                        0.2496, 0.2496, 0.2496,
                                                                        0.0624, 0.0624, 0.0624,
                                                                        10])
                    if obtiene[0].lower() == "monedas":
                        print("Obtiene:", obtiene[0].capitalize())
                        time.sleep(0.7)
                    else:
                        posibles = []
                        for personaje, categoria in personajes.items():
                            if categoria == obtiene[0] and personaje not in posibles and obtiene[0].lower() not in poseePersonajes:
                                posibles.append(personaje)

                        repetir = True
                        repeticiones = 0
                        while repetir:
                            obtiene = random.choice(posibles)
                            if obtiene not in poseePersonajes:
                                poseePersonajes.append(obtiene.lower())
                                print("Obtiene:", obtiene.capitalize())
                                time.sleep(0.7)
                                self.setPersonajes(personajes[obtiene], obtiene)
                                repetir = False
                            else:
                                repetir = True

                            repeticiones += 1
                            if repeticiones > len(posibles):
                                print("Obtiene: Monedas")
                                time.sleep(0.7)
                                repetir = False

    def setPersonajes(self, categoria, nombre):
        with open(self.nombre, "a") as f:
            f.write(categoria + "\n")
            f.write(nombre + "\n")

    def getPersonajes(self):
        personajes = {}

        with open("brawlers", "r+") as f:
            lineas = f.readlines()
            lineas_iter = iter(lineas)
            numLinea = 1
            for linea in lineas_iter:
                if numLinea / 2 != 0:
                    personajes[next(lineas_iter).rstrip()] = linea.rstrip()
                numLinea += 1
        return personajes

if __name__ == "__main__":
    try:
        while True:
            nombreJugador = input("Nombre del jugador: ")
            jugador = Jugador(nombreJugador)
            archivo = jugador.crearArchivo()
            archivo

            while True:
                eleccionJugador = input("¿Qué quiere hacer? (fin para ver el archivo, simular N para abrir cajas, [ctrl+C] para salir): ")
                eleccionJugadorSplit = eleccionJugador.split()
                if eleccionJugador == "fin":
                    print("\nEl archivo del jugador", nombreJugador, "está listo.\n¡Hasta la próxima!")
                    exit()
                elif len(eleccionJugadorSplit) == 2 and eleccionJugadorSplit[0] == "simular" and eleccionJugadorSplit[1] and isinstance(int(eleccionJugadorSplit[1]), int):
                    jugador.abrirCaja(eleccionJugadorSplit[1])
                else:
                    print("Acción no reconocida o inválida. Inténtelo de nuevo.\n")

            break
    
    except KeyboardInterrupt:
        print("\n\nDeteniendo la ejecución...")
        time.sleep(0.2)
        print("¡Hasta la próxima!")