# Introducido por teclado un número entero mayor que 2, visualizarlo de todas las formas posibles como producto de dos factores (no es válido el número 1 como factor).

num = int(input("Introduce un número: "))

contador = 2

while contador in range(num):
    if num%contador == 0:
        print(num/contador, "*", contador)

    contador += 1