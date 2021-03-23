# Escribe un programa que solicite tres números al usuario y muestre el mayor de ellos.

try:
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))
    num3 = int(input("Introduce el tercer número: "))
    
    if num1 > num2 and num1 > num3:
        mayor = num1
    elif num2 > num1 and num2 > num3:
        mayor = num2
    elif num3 > num1 and num3 > num2:
        mayor = num3

    print("El número mayor es:", mayor)

except ValueError:
    print("Debes introducir un carácter válido.")