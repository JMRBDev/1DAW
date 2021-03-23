# Crear una función que reciba como parámetro el nombre de un archivo en formato CSV y devuelva una lista de
# diccionarios con los datos del archivo.
# En la primera línea de los archivos CSV se encuentran los nombres de las columnas que pueden servir como
# claves de los diccionarios.

import sys
import csv

def showDict():
    with (open(filename, mode='r', encoding='utf-8')) as f:
        rd = csv.DictReader(f, delimiter=',')
        for row in rd:
            print(row)

if __name__ == '__main__':
    filename = sys.argv[1]
    
    showDict()