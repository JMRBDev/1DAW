# Crear una función que calcule la suma de la progresión geométrica: 1 + x + x2 + x3 + . . . + xn

def suma(x, n):

    solucion = 0

    for i in range(n):
        solucion += x**n

    return "La suma de tu progresion es {}".format(solucion)

print(suma(2, 10))