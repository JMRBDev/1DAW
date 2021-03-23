# La WDA organiza una liga de baloncesto en la que participan 6 equipos:
# 1. Chiclana Blues (CHB)
# 2. Cádiz Wheels (CAW)
# 3. Caleta Surfers (CSU)
# 4. Conil Suns (COS)
# 5. Victoria Bedouins (VIB)
# 6. Cortadura Hearts (CHE)
# Debemos realizar un programa para mantener la clasificación de estos equipos de la siguiente forma:
# • Se mostrará la clasificación y se pedirá un resultado hasta que el usuario introduzca “fin”
# • Los resultados estarán en el formato EQ1 PUNTOS1 EQ2 PUNTOS2
# • Para denominar los equipos se puede usar cualquiera de sus palabras, sus iniciales o el nombre completo. Por
# ejemplo, para introducir el resultado de un partido donde jueguen los Conil Suns se puede usar Conil, Suns,
# COS o Conil Suns.
# • El formato de la clasificación será el siguiente:
# Equipo P.J. P.G. P.P. P.A.F. P.E.C. MAR
# COS 3 2 1 256 235 +7
# ...
# Donde:
# P.J. Partidos jugados P.G. Partidos ganados P.P. Partidos perdidos
# P.A.F. Puntos a favor P.E.C. Puntos en contra MAR Margen de victoria/ derrota
# El margen de victoria/derrota puede ser positivo o negativo, dependiendo si el equipo marca más o menos
# puntos de los que recibe.
# • El orden de la clasificación será por número de victorias, a igual número de victorias menor número de
# derrotas y si empatan en las dos anteriores por margen de victoria. Si se mantiene el empate se ordenarán
# por puntos a favor y si aún sigue el empate por orden alfabético.

nombres = {"Chiclana Blues":    "CHB",
           "Cádiz Wheels":      "CAW",
           "Caleta Surfers":    "CSU",
           "Conil Suns":        "COS",
           "Victoria Bedouins": "VIB",
           "Cortadura Hearts":  "CHE"}

equipos = {"CHB":   {"P.J":0, "P.G":1, "P.P":0, "P.A.F":5, "P.E.C":3, "M.A.R":4}, 
           "CAW":   {"P.J":1, "P.G":3, "P.P":5, "P.A.F":4, "P.E.C":2, "M.A.R":0},
           "CSU":   {"P.J":2, "P.G":2, "P.P":4, "P.A.F":1, "P.E.C":0, "M.A.R":3},
           "COS":   {"P.J":3, "P.G":4, "P.P":3, "P.A.F":2, "P.E.C":1, "M.A.R":5},
           "VIB":   {"P.J":5, "P.G":5, "P.P":2, "P.A.F":3, "P.E.C":4, "M.A.R":1},
           "CHE":   {"P.J":4, "P.G":0, "P.P":1, "P.A.F":0, "P.E.C":3, "M.A.R":2}}

def mostrarPuntosPorPG(listaEquipos): # Orden principal
    print("Equipo\t\tP.J\t\tP.G\t\tP.P\t\tP.A.F\t\tP.E.C\t\tM.A.R")
    ordenadoPG = sorted(listaEquipos.items(), key=lambda x: x[1]["P.G"], reverse=True)
    for i in ordenadoPG:
        print(i[0], *i[1].values(), sep="\t\t")

def mostrarPuntosPorPP(listaEquipos): # Si empatan a victorias, menos derrotas primero
    print("Equipo\t\tP.J\t\tP.G\t\tP.P\t\tP.A.F\t\tP.E.C\t\tM.A.R")
    ordenadoPP = sorted(listaEquipos.items(), key=lambda x: x[1]["P.P"], reverse=False)
    for i in ordenadoPP:
        print(i[0], *i[1].values(), sep="\t\t")

def mostrarPuntosPorMAR(listaEquipos): # Si empatan a victorias y derrotas, mayor M.A.R primero
    print("Equipo\t\tP.J\t\tP.G\t\tP.P\t\tP.A.F\t\tP.E.C\t\tM.A.R")
    ordenadoMAR = sorted(listaEquipos.items(), key=lambda x: x[1]["M.A.R"], reverse=True)
    for i in ordenadoMAR:
        print(i[0], *i[1].values(), sep="\t\t")

def mostrarPuntosPorPAF(listaEquipos): # Si empatan a lo anterior, mayor P.A.F primero
    print("Equipo\t\tP.J\t\tP.G\t\tP.P\t\tP.A.F\t\tP.E.C\t\tM.A.R")
    ordenadoPAF = sorted(listaEquipos.items(), key=lambda x: x[1]["P.A.F"], reverse=True)
    for i in ordenadoPAF:
        print(i[0], *i[1].values(), sep="\t\t")

def mostrarPuntosPorAlfabeto(listaEquipos): # Si empatan a todo, por orden alfabético
    print("Equipo\t\tP.J\t\tP.G\t\tP.P\t\tP.A.F\t\tP.E.C\t\tM.A.R")
    ordenadoAlf = sorted(listaEquipos.keys(), key=str.lower, reverse=False)
    for i in ordenadoAlf:
        print(i, *list(equipos[i].values()), sep="\t\t")

print("Por P.G")
mostrarPuntosPorPG(equipos)
print("\n")
print("Por P.P")
mostrarPuntosPorPP(equipos)
print("\n")
print("Por M.A.R")
mostrarPuntosPorMAR(equipos)
print("\n")
print("Por P.A.F")
mostrarPuntosPorPAF(equipos)
print("\n")
print("Por orden alfabético")
mostrarPuntosPorAlfabeto(equipos)

#if __name__ == "__main__":
#    comprobacionIguales = []
#    for i in list(equipos.keys()):
#        print(list(equipos.values())[0].values())
#        #comprobacionIguales.append()
#    print(comprobacionIguales)