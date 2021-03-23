# Utilizando las funciones creadas en los ejercicios anteriores crear un programa que permita consultar y extraer
# las temperaturas medias el día 31/12/2018 de todas las estaciones meteorológicas de una provincia
# determinada usando los archivos .csv que se suministran:
# ListadoEstaciones2018-08.csv
# Se debe usar para mostrar las provincias donde existen estaciones meteorológicas al usuario.
# Aemet2018-12-31.csv
# Se usará para extraer las temperaturas.
# El programa deberá mostrar las provincias con estaciones meteorológicas al usuario, que deberá elegir una de
# ellas, indicándole el programa si no es correcta. Tras una elección correcta se le debe solicitar al usuario el
# nombre del archivo donde se guardarán los datos de estas estaciones en formato csv. Si el archivo existe debe
# pedir confirmación de sobreescritura.

import os
import csv

def checkIfExists(province):
    global provinceIndex
    with open(f'{os.path.dirname(os.path.abspath(__file__))}\\ListadoEstaciones2018-08.csv', mode='r', encoding='utf-8') as f:
        counter = 1
        for line in f:
            provincesList = line.split(',')
            provincesList[-1] = provincesList[-1].strip()
            print(provincesList)
            if province in provincesList:
                provinceIndex = provincesList.index(province)
                return True
            
            counter -= 1
            if counter == 0:
                return False

def saveData(filePath):
    columns = []
    with open(f'{os.path.dirname(os.path.abspath(__file__))}\\ListadoEstaciones2018-08.csv', mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if columns:
                for i, value in enumerate(row):
                    columns[i].append(value)
            else:
                columns = [[value] for value in row]

    tempsList = columns[provinceIndex][1::]
    tempsList = [int(x) for x in tempsList]
    return str(sum(tempsList) / len(tempsList))


if __name__ == '__main__':
    while True:
        userInput = input('Escoja una provincia: ')

        if checkIfExists(userInput) == False: # Ver si la provincia NO está registrada en el Listado de Estaciones
            print('La provincia no está en el registro.')
        else: # Si la provincia está registrada:
            saveFilePath = input('Introduzca la ruta al archivo de guardado: ')
            
            if os.path.exists(saveFilePath) == True and os.path.splitext(saveFilePath)[1] == '.csv': # Si el archivo existe y es un .CSV:
                confirmation = input('El archivo ya existe, ¿Desea sobreescribirlo? (Y/N): ')
            
                if confirmation.lower() == 'y': # Confirmar sobreescritura
                    with open(f'{os.path.dirname(os.path.abspath(__file__))}\\{saveFilePath}', mode='w', encoding='utf-8') as f:
                        f.write(saveData(saveFilePath))
                        print('Datos guardados con éxito.')
                else: # Sobreescritura denegada
                    print('Ha escogido NO sobreescribir el archivo. Cancelando operación.')
            
            elif os.path.exists(saveFilePath) == False and os.path.splitext(saveFilePath)[1] == '.csv': # Si el archivo NO existe y se quiere crear un .CSV:
                with open(f'{os.path.dirname(os.path.abspath(__file__))}\\{saveFilePath}', mode='w', encoding='utf-8') as f:
                    f.write(saveData(saveFilePath))
                    print('Datos guardados con éxito.')
            else: # Si el archivo NO es un .CSV:
                print('El archivo debe tener extensión .csv')