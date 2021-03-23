# Diseña un programa que, dados dos números enteros, muestre por pantalla uno de estos mensajes: "El segundo es el cuadrado exacto del primero.", "El segundo es menor que el cuadrado del primero." o "El segundo es mayor que el cuadrado del primero.", dependiendo de la verificación de la condición correspondiente al significado de cada mensaje.

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

if num1**2 == num2:
    print("El segundo es el cuadrado exacto del primero.")
elif num1**2 > num2:
    print("El segundo es menor que el cuadrado del primero.")
elif num1**2 < num2:
    print("El segundo es mayor que el cuadrado del primero.")