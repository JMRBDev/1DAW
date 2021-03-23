# Crear una función que reciba como parámetro el nombre de un archivo y una lista de diccionarios y almacene
# los datos de los diccionarios en el archivo en formato CSV.
# En la primera línea de los archivos CSV se encuentran los nombres de las columnas que deben ser las claves del
# diccionario.

import sys
import csv

def saveDict():
    with (open(filename, mode='w', encoding='utf-8')) as f:
        for key in my_dict.keys():
            f.write("%s,%s,"%(key,my_dict[key]))


if __name__ == '__main__':
    filename = sys.argv[1]
    my_dict = {'Nombre':'Antonio', 'Apellido':'Gutiérrez', 'Edad':23, 'Ciudad':'Málaga'}
    saveDict()