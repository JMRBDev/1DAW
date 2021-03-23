# Encuentra los errores en el siguiente código:

##### j = input("numero: ")
##### for class in range(1, 5, -1):
##### print(class+j)

# La palabra "class" es una palabra reservada de Python, y no se puede usar para nombrar una variable.
# La variable j debe ser un número entero (int).
# La línea del print debe estar identada para que entre dentro del bucle for.
# El rango con step negativo debe tener el valor más alto en el primer lugar, y el más bajo en el segundo.

# Código corregido:
j = int(input("numero: "))
for i in range(5, 1, -1):
    print(i+j)