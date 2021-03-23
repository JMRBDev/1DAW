# Dados dos números enteros (un dividendo y un divisor distinto de 0) obtener su cociente y el resto mediante restas sucesivas.

contador = int(0)

dividendo = int(input("Introduce el dividendo: "))
divisor = int(input("Introduce el divisor: "))

dividendo -= divisor

while dividendo >= 0:
    contador += 1
    dividendo -= divisor

print("La división es igual a:", str(contador))