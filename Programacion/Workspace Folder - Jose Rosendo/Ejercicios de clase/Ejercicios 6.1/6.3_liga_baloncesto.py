# Modificar el diseño e implementación del Ejercicio 4.10 (clasificación de equipos de baloncesto) usando
# tecnologías de programación orientada a objetos.
# Puede ser necesario definir varias clases para completarlo.
# También se debe aumentar las prestaciones del programa guardando los resultados y permitiendo mostrar la
# lista de resultados cargados. Para acceder a esta lista se introducirá “calendario” en lugar del resultado de un
# partido. De cada partido se debe almacenar la fecha (para evitar demasiados cambios, siempre será la fecha
# actual en el momento de cargar el resultado).
# Para gestionar las fechas se deben usar las librería Python de control de fechas: datetime y calendar.

class Equipo:
    nombre = ''
    abreviacion = ''
    pj = 0
    pg = 0
    pp = 0
    paf = 0
    pec = 0
    mar = 0

    def agregarResultados(self, pj, pg, pp, paf, pec, mar):
        self.pj = pj
        self.pg = pg
        self.pp = pp
        self.paf = paf
        self.pec = pec
        self.mar = mar

    def __init__(self, nombre, abreviacion):
        self.nombre = nombre
        self.abreviacion = abreviacion

class Clasificacion:
    resultados = []

    def __init__(self, equipo1, equipo2, equipo3, equipo4, equipo5, equipo6):
        self.orden = [equipo1, equipo2, equipo3, equipo4, equipo5, equipo6]

    def mostrar(self, equipos, pj, pg, pp, paf, pec, mar):
        print('Equipo\t\tP.J\tP.G\tP.P\tP.A.F\tP.E.C\tM.A.R')
        self.orden = sorted(self.orden, key=lambda x: (-x.pg, x.pp, -x.mar, -x.paf, -x.abreviacion))
        for i in self.orden:
            print(i.abreviacion, '\t\t', i.pj, '\t', i.pg, '\t', i.pp, '\t', i.paf, '\t', i.pec, '\t', i.mar)


if __name__ == '__main__':
    equipo1 = Equipo('Chiclana Blues', 'CHB')
    equipo2 = Equipo('Cádiz Wheels', 'CAW')
    equipo3 = Equipo('Caleta Surfers', 'CSU')
    equipo4 = Equipo('Conil Suns', 'COS')
    equipo5 = Equipo('Victoria Bedouins', 'VIB')
    equipo6 = Equipo('Cortadura Hearts', 'CHE')
    tabla = Clasificacion(equipo1, equipo2, equipo3, equipo4, equipo5, equipo6)

    while True:
        userInput = input('¿Qué quieres hacer? (Agregar, Mostrar, Salir)')
        if userInput.lower() == 'salir':
            exit()
        elif userInput.lower() == 'agregar':
            teamSelection = input(f'¿De qué equipo?\n{equipo1.abreviacion}, {equipo2.abreviacion}, {equipo3.abreviacion}, {equipo4.abreviacion}, {equipo5.abreviacion}, {equipo6.abreviacion}: ')
            if teamSelection.upper() == equipo1.abreviacion:
                equipo1.agregarResultados(int(input('P.J: ')),
                                          int(input('P.G: ')),
                                          int(input('P.P: ')),
                                          int(input('P.A.F: ')),
                                          int(input('P.E.C: ')),
                                          int(input('M.A.R: ')))
            elif teamSelection.upper() == equipo2.abreviacion:
                equipo2.agregarResultados(int(input('P.J: ')),
                                          int(input('P.G: ')),
                                          int(input('P.P: ')),
                                          int(input('P.A.F: ')),
                                          int(input('P.E.C: ')),
                                          int(input('M.A.R: ')))
            elif teamSelection.upper() == equipo3.abreviacion:
                equipo3.agregarResultados(int(input('P.J: ')),
                                          int(input('P.G: ')),
                                          int(input('P.P: ')),
                                          int(input('P.A.F: ')),
                                          int(input('P.E.C: ')),
                                          int(input('M.A.R: ')))
            
            elif teamSelection.upper() == equipo4.abreviacion:
                equipo4.agregarResultados(int(input('P.J: ')),
                                          int(input('P.G: ')),
                                          int(input('P.P: ')),
                                          int(input('P.A.F: ')),
                                          int(input('P.E.C: ')),
                                          int(input('M.A.R: ')))
            
            elif teamSelection.upper() == equipo5.abreviacion:
                equipo5.agregarResultados(int(input('P.J: ')),
                                          int(input('P.G: ')),
                                          int(input('P.P: ')),
                                          int(input('P.A.F: ')),
                                          int(input('P.E.C: ')),
                                          int(input('M.A.R: ')))
            
            elif teamSelection.upper() == equipo6.abreviacion:
                equipo6.agregarResultados(int(input('P.J: ')),
                                          int(input('P.G: ')),
                                          int(input('P.P: ')),
                                          int(input('P.A.F: ')),
                                          int(input('P.E.C: ')),
                                          int(input('M.A.R: ')))
            else:
                print(f'El equipo {teamSelection} no existe.')
        elif userInput.lower() == 'mostrar':
            tabla.mostrar([equipo1.abreviacion, equipo2.abreviacion, equipo3.abreviacion, equipo4.abreviacion, equipo5.abreviacion, equipo6.abreviacion],
                          [equipo1.pj, equipo2.pj, equipo3.pj, equipo4.pj, equipo5.pj, equipo6.pj],
                          [equipo1.pg, equipo2.pg, equipo3.pg, equipo4.pg, equipo5.pg, equipo6.pg],
                          [equipo1.pp, equipo2.pp, equipo3.pp, equipo4.pp, equipo5.pp, equipo6.pp],
                          [equipo1.paf, equipo2.paf, equipo3.paf, equipo4.paf, equipo5.paf, equipo6.paf],
                          [equipo1.pec, equipo2.pec, equipo3.pec, equipo4.pec, equipo5.pec, equipo6.pec],
                          [equipo1.mar, equipo2.mar, equipo3.mar, equipo4.mar, equipo5.mar, equipo6.mar])