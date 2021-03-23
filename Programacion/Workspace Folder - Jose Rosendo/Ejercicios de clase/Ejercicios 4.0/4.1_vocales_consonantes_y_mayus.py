# Introducir una cadena por teclado e imprimirla sin vocales, sin consonantes y con las vocales en mayúsculas (las consonantes deben quedarse tal como estén).

cad = str(input("Introduce una cadena de caracteres: ").lower())
vocales_list = ["a", "e", "i", "o", "u"]

consonantes = []
vocales = []
minus_y_mayus = []

for i in cad:
    if i not in vocales_list:
        consonantes.append(i)

for i in cad:
    if i in vocales_list:
        vocales.append(i)

for i in cad:
    if i not in vocales_list:
        minus_y_mayus.append(i)
    else:
        minus_y_mayus.append(i.upper())

print(*consonantes)
print(*vocales)
print(*minus_y_mayus)