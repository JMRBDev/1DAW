# Crear una función denominada hay_duplicados que reciba una lista y devuelva True si contiene duplicados o False si no es así. Usar la función para generar una lista de 20 números aleatorios del 1 al 100 que no contenga duplicados.

import random

def hay_duplicados(lista):
    for item in lista:
        if lista.count(item) == 1:
            esCorrecto = True
        else:
            esCorrecto = False
            break
    
    return not esCorrecto

lista = []
for i in range(99):
    lista.append(random.randint(1, 100))

print(hay_duplicados([lista]))