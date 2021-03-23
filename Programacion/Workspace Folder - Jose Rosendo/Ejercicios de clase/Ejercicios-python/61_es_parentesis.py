# Diseña un programa que lea un carácter de teclado y muestre por pantalla el mensaje "Es paréntesis" sólo si el carácter leído es un paréntesis abierto o cerrado.

caracter = input("Introduce un carácter: ")

if caracter == "(" or caracter == ")":
    print("Es paréntesis")
else:
    pass