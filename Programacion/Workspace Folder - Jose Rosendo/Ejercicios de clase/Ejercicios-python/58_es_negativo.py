# Diseña un programa que lea un número flotante por teclado y muestre por pantalla el mensaje "El número es negativo." sólo si el número es menor que cero.

num = float(input("Introduce un número: "))

if num < 0:
    print("El número es negativo.")
elif num >= 0:
    print("El número es positivo.")