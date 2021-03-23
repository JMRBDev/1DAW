# Determinar si dos números enteros positivos son amigos, es decir, si la suma de los divisores del 1o excepto el mismo es igual al 2o, y viceversa.

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

divisoresNum1 = []
divisoresNum2 = []

sumaDivisores1 = int

for i in range(1, num1):
    if num1%i == 0:
        divisoresNum1.append(int(i))
    else:
        pass

for i in range(1, num2):
    if num2%i == 0:
        divisoresNum2.append(int(i))
    else:
        pass

totalDivisoresNum1 = sum(divisoresNum1)
totalDivisoresNum2 = sum(divisoresNum2)

print("\nDivisores de ", num1, ": ", divisoresNum1, sep="")
print("La suma de todos los divisores de", num1, "es:", totalDivisoresNum1, "\n")

print("Divisores de ", num2, ": ", divisoresNum2, sep="")
print("La suma de todos los divisores de", num2, "es:", totalDivisoresNum2, "\n")

if totalDivisoresNum1 == num2:
    print(num1, "es amigo de", num2)
else:
    print(num1, "no es amigo de", num2)

if totalDivisoresNum2 == num1:
    print(num2, "es amigo de", num1)
else:
    print(num2, "no es amigo de", num1)