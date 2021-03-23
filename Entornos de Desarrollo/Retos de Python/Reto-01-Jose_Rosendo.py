# Sin ejecutarlo, ¿qué hace este código?
# Encuentra y arregla el fallito.

strng = "Hello Hello, Welcome Welcome to python.advance.projects and start learning python"

words = strng.split()
d = {}.fromkeys(words, 0)
for w in words:
    d[w] += 1
print(d)


"""
- Jose Rosendo -
Este archivo convierte la String strng a lista separando las palabras por los espacios entre ellas.
Luego pasa esa lista a un diccionario, siendo cada palabra de la lista una clave, y de valor toman un Integer 0.
El bucle recorre la lista de palabras, y para cada palabra, suma 1 a su valor correspondiente en el diccionario.

Al final se imprime el diccionario. El resultado es una cuenta de las veces que se repite cada palabra en la String strng.

El problema que he encontrado es que en la segunda palabra del String strng hay una coma pegada al Hello, por tanto
la separación no tiene en cuenta que Hello sale 2 veces, y no 1.

Una posible solución a este problema es la siguiente:
"""


import re

strng = "Hello Hello, Welcome Welcome to python.advance.projects and start learning python"

strng = re.sub(r'[^\w]', ' ', strng)
words = strng.split()
d = {}.fromkeys(words, 0)
for w in words:
    d[w] += 1
print(d)


"""
De esta manera eliminamos cualquier simbolo de la String strng y cuenta las palabras correctamente
"""