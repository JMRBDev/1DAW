# Usando un bucle while, mostrar en pantalla la serie: 1, 50, 3, 48, 5, 46, 7, 44........., 0.

num1 = int(input("Introduce el primer número de la serie: "))
num2 = int(input("Introduce el último número de la serie: "))

numMin = num1-1
numMax = num2+1

separacion = ", "

while num1 <= numMax and num2 >= numMin:
    if num2 == numMin:
        separacion = "."
    print(num1, end=", ")
    print(num2, separacion, sep="", end="")
    num1 += 2
    num2 -= 2