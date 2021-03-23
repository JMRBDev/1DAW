import datetime

class Concesionario:
    nombre = str
    marcas = list

    def __init__(self, nombre, marcas):
        self.nombre = nombre
        self.marcas = marcas

    def __repr__(self):
        cadena = str(self.nombre) + " - " + str(self.marcas)
        return cadena

    def buscar(self, busqueda):
        marca = busqueda.marca
        modelo = busqueda.modelo
        combustible = busqueda.combustible
        min_potencia = busqueda.min_potencia
        max_kilometros = busqueda.max_kilometros
        min_ano = busqueda.min_ano

        resultado = []
        for marca in self.marcas:
            for coche in marca.coches:
                if marca.marca == marca and coche.modelo == modelo and coche.combustible == combustible and coche.min_potencia == min_potencia and coche.max_kilometros == max_kilometros and coche.min_ano == min_ano:
                    resultado.append(coche)

        return resultado

class Marca:
    marca = str
    nacionalidad = str
    coches = list

    def __init__(self, marca, nacionalidad, coches):
        self.marca = marca
        self.nacionalidad = nacionalidad
        self.coches = coches

    def __repr__(self):
        cadena = str(self.marca) + " - " + str(self.nacionalidad) + " - " + str(self.coches)
        return cadena

class Coche:
    modelo = str
    cilindrada = float
    combustible = str
    potencia = int
    matricula = str
    fecha = datetime.date
    kilometros = int

    def __init__(self, modelo, cilindrada, combustible, potencia, matricula, fecha, kilometros):
        self.modelo = modelo
        self.cilindrada = cilindrada
        self.combustible = combustible
        self.potencia = potencia
        self.matricula = matricula
        self.fecha = fecha
        self.kilometros = kilometros

    def __repr__(self):
        cadena = str(self.modelo) + " - " + str(self.cilindrada) + " - " + str(self.combustible) + " - " + str(self.potencia) + " - " + str(self.matricula) + " - " + str(self.fecha) + " - " + str(self.kilometros)
        return cadena

class Busqueda:
    marca = str
    modelo = str
    combustible = str
    min_potencia = int
    max_kilometros = int
    min_ano = int

    def __init__(self, marca, modelo, combustible, min_potencia, max_kilometros, min_ano):
        self.marca = marca
        self.modelo = modelo
        self.combustible = combustible
        self.min_potencia = min_potencia
        self.max_kilometros = max_kilometros
        self.min_ano = min_ano

    def __repr__(self):
        cadena = str(self.marca) + " - " + str(self.modelo) + " - " + str(self.combustible) + " - " + str(self.min_potencia) + " - " + str(self.max_kilometros) + " - " + str(self.min_ano)
        return cadena