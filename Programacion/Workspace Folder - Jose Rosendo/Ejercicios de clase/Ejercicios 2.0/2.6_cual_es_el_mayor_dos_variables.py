# Escribe el programa anterior usando solamente dos variables. // Lo he hecho con una.

try:
    nums = [int(input("Introduce el primer número: ")), int(input("Introduce el segundo número: ")), int(input("Introduce el tercer número: "))]
    nums.sort()

    print("El número mayor es:", nums[-1])

except ValueError:
    print("Debes introducir un carácter válido.")