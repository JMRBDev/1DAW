# Escribe un programa genérico para búsqueda en un archivo: pygrep.
# El programa debe aceptar como argumentos de llamada desde la línea de comandos el contenido a buscar, el
# nombre del archivo y las opciones.
# Como resultado mostrará las líneas que contienen el patrón.
# Si se utiliza la opción -l mostrará también el número de línea junto a la línea localizada.
# Si se utiliza la opción -t mostrará al final de la búsqueda el total de repeticiones localizadas y el número de líneas
# donde aparecen.

import sys

def showLines(): # No options
    with open(fileName, 'r', encoding='utf8') as f:
        for line in f:
            if contentToSearch in line:
                print(line)

def showLineNumber(): # -l
    counter = 0

    with open(fileName, 'r', encoding='utf8') as f:
        for line in f:
            counter += 1
            if contentToSearch in line:
                print(f"{counter}.- {line}")

def showNumberOfReps(): # -t
    repsCounter = 0
    linesCounter = 0

    with open(fileName, 'r', encoding='utf8') as f:
        for line in f:
            if contentToSearch in line:
                repsCounter += line.count(contentToSearch)
                linesCounter += 1
    
    return f"Total matches: {repsCounter}\nLines with matches: {linesCounter}"


if __name__ == "__main__":
    contentToSearch = sys.argv[1]
    fileName = sys.argv[2]

    if len(list(sys.argv)) != 4:
        showLines()
    elif len(list(sys.argv)) == 4 and sys.argv[3] == "-l":
        options = sys.argv[-1]
        showLineNumber()
    elif len(list(sys.argv)) == 4 and sys.argv[3] == "-t":
        options = sys.argv[-1]
        showLines()
        print("\n"+showNumberOfReps())
    else:
        print("An error occurred.\nUsage: python 'contentToSearch' fileName [-l/-t]")