# Pide un número y determina si es el doble de un número par o un número impar

num = int(input("Introduce un número: "))
mitadNum = num/2

if mitadNum%2:
    print("Es doble de un número impar")
else:
    print("Es doble de un número par")