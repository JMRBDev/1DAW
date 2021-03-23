import random
import string

lineas = {}
for linea in range(0, 50):
    lineas["linea{0}".format(linea)] = [x for x in random.choices(string.ascii_uppercase, k=50)]

with open("tablero", "w", encoding="utf-8") as f:
    for linea in lineas.values():
        linea = str(" ".join(linea)) + "\n"
        f.write(linea)

with open("puntos", "w", encoding="utf-8") as f:
    lineasPuntos = {}
    for lineaPuntos in range(0, 50):
        for punto in range (0, 50):
            lineasPuntos["linea{0}".format(lineaPuntos)] = "."
    
    f.write(str(lineasPuntos.values()))

listaPalabras = []
def cargarPalabras():
    with open("palabras", "r", encoding="utf-8") as f:
        for line in f:
            listaPalabras.append(line.strip())

def sortearPalabras(listaPalabras):
    random.shuffle(listaPalabras)
    palabras = listaPalabras[:10]
    
    return palabras

verticales = []
horizontales = []
def seleccionarVerHor(listaPalabras):
    global cantidadVerticales
    cantidadVerticales = random.randint(0, 10)
    aux = 0
    while aux != cantidadVerticales:
        verticales.append(listaPalabras[aux])
        aux += 1

    for horizontal in listaPalabras[cantidadVerticales:10]:
        horizontales.append(horizontal)

    return (verticales, horizontales)

def meterPalabras(palabrasVer, palabrasHor):
    print("----- VERTICALES -----")
    if len(palabrasVer) == 0:
        print("No hay palabras en disposición vertical.")
    else:
        for palabra in palabrasVer:
            celdaInicial = [random.randint(0, 49 - len(palabra)), random.randint(0, 49)] # Filas, Columnas
            print(f"Fila {celdaInicial[0]} y Columna {celdaInicial[1]} --> {palabra}")
            list(palabra)
            for letra in range(len(palabra)):
                lineas["linea{}".format(celdaInicial[0])][celdaInicial[1]] = palabra[letra]
                celdaInicial[0] += 1

    print("\n----- HORIZONTALES -----")
    if len(palabrasHor) == 0:
        print("No hay palabras en disposición horizontal.")
    else:
        for palabra in palabrasHor:
            celdaInicial = [random.randint(0, 49), random.randint(0, 49 - len(palabra))] # Filas, Columnas
            print(f"Fila {celdaInicial[0]} y Columna {celdaInicial[1]} --> {palabra}")
            list(palabra)
            for letra in range(len(palabra)):
                lineas["linea{}".format(celdaInicial[0])][celdaInicial[1]] = palabra[letra]
                celdaInicial[1] += 1

def imprimirTablero():
    print("\n")
    for i in lineas.values():
        print(*i)

cargarPalabras()
print("Palabras a buscar:", *sortearPalabras(listaPalabras), end="\n\n")
print(seleccionarVerHor(listaPalabras))
meterPalabras(verticales, horizontales)
imprimirTablero()