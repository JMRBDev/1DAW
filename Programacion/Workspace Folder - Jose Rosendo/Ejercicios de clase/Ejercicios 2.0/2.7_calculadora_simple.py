# Escribe un programa que solicite dos números al usuario y le permita decidir si sumarlos, restarlos, multiplicarlos o dividirlos. El programa debe controlar todos los errores posibles

try:
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    operacion = str(input("Operación a realizar (+, -, *, /): "))
    
    if operacion == "+":
        print(num1+num2)
    elif operacion == "-":
        print(num1-num2)
    elif operacion == "*":
        print(num1*num2)
    elif operacion == "/":
        print(num1/num2)

except ValueError:
    print("Debes introducir un carácter de tipo válido.")
except ZeroDivisionError:
    print("No puedes dividir entre cero.")