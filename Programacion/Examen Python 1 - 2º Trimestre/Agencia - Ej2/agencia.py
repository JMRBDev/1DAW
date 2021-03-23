import datetime

class Agencia:
    nombre = str
    eventos = list

    def __init__(self, nombre, eventos):
        self.nombre = nombre
        self.eventos = eventos

    def __str__(self):
        cadena = str(self.nombre) + " - " + str(self.eventos)
        return cadena

    def reservar(self, evento, personas, fecha):
        pass # El enunciado no dice nada sobre lo que tiene que hacer esta función

class Evento:
    denominacion = str
    fecha = datetime.date
    lugar = list
    dias = int
    precio_entrada = float

    def __init__(self, denominacion, fecha, lugar, dias, precio_entrada):
        self.denominacion = denominacion
        self.fecha = fecha
        self.lugar = lugar
        self.dias = dias
        self.precio_entrada = precio_entrada

    def __str__(self):
        cadena = str(self.denominacion) + " en " + str(self.lugar.nombre) + " a " + str(self.precio_entrada) + "€"
        return cadena

    def precioPersona(self, fecha, numeroAsistentes):
        # Precio entradas = PrecioUnaEntrada * Asistentes
        # Precio estancia = Dias * PrecioEstancia * Asistentes
        # Precio transporte = DistanciaCiudad * 0.12 * Asistentes

        precioEntradas = float(self.precio_entrada) * numeroAsistentes
        precioEstancias = self.dias * float(self.lugar.precio_estancia) * numeroAsistentes
        precioTransportes = float(self.lugar.distancia) * 0.12 * numeroAsistentes
        
        # Precio asistencia (Total) = Entradas + Estancia + Transporte
        return float(precioEntradas + precioEstancias + precioTransportes)

class Ciudad:
    nombre = str
    distancia = int
    precio_estancia = float

    def __init__(self, nombre, distancia, precio_estancia):
        self.nombre = nombre
        self.distancia = distancia
        self.precio_estancia = precio_estancia

    def __str__(self):
        cadena = str(self.nombre) + " - " + str(self.distancia) + " - " + str(self.precio_estancia)
        return cadena

class Viaje:
    personas = int
    precio = float
    evento = ""

    def __init__(self, personas, precio, evento):
        self.personas = personas
        self.precio = precio
        self.evento = evento

    def __str__(self):
        cadena = str(self.personas) + " - " + str(self.precio) + " - " + str(self.evento)
        return cadena