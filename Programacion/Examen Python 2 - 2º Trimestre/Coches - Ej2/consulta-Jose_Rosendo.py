from datetime import datetime
from concesionario import *

if __name__ == "__main__":
    coches1 = [ Coche("V40", 2.0, "Diesel", 120, "", datetime.date(2019,2,2), 0),
                Coche("S90", 2.0, "Diesel", 150, "", datetime.date(2017,11,15), 23435) ]
    coches2 = [ Coche("A3", 1.0, "Gasolina", 115, "", datetime.date(2018,8,5), 1453),
                Coche("A4", 2.0, "Gasolina", 125, "", datetime.date(2019,4,4), 0) ]
    coches3 = [ Coche("Corolla", 1.5, "Híbrido", 115, "", datetime.date(2018,7,5), 7564),
                Coche("C-HR", 1.8, "Híbrido", 125, "", datetime.date(2019,2,3), 0) ]
    marcas = [ Marca("Volvo", "Suecia", coches1),
            Marca("Audi", "Alemania", coches2),
            Marca("Toyota", "Japón", coches3) ]
    concesionario = Concesionario("Rafael Multimotor", marcas)

    busquedaMarca = input("Marca: ")
    busquedaModelo = input("Modelo: ")
    busquedaCombustible = input("Combustible: ")
    busquedaPotencia = int(input("Potencia: "))
    busquedaMaxKm = int(input("Kilometros máximos: "))
    busquedaMinAno = datetime.datetime.strptime(input("Año mínimo: "), '%d-%m-%Y')

    resultado = concesionario.buscar(Busqueda(busquedaMarca, busquedaModelo, busquedaCombustible, busquedaPotencia, busquedaMaxKm, busquedaMinAno))

    if len(resultado) == 0:
        print("\nNo se han encontrado coincidencias")
    else:
        for coche in resultado:
            print(coche)