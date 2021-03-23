# Escribe un programa que solicite un número al usuario e indique si es par o impar.

try:
    num = int(input("Introduce un número: "))

    if num%2 == 0:
        print("El número es par.")
    else:
        print("El número es impar.")
except ValueError:
    print("Debes introducir un carácter válido.")