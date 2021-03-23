# Dado un número entero positivo hallar los números perfectos menores que él. Un número es perfecto si la suma de sus divisores, excepto él mismo, es igual al propio número.

num1 = int(input("Introduce el primer número: "))

divisoresNum1 = []

sumaDivisores1 = int

while num1 >= 0:
    for i in range(1, num1):
        if num1%i == 0:
            divisoresNum1.append(int(i))
        else:
            pass

    del divisoresNum1[0]
    totalDivisoresNum1 = sum(divisoresNum1)

    if totalDivisoresNum1 == num1:
        print(num1, "es perfecto")
    else:
        divisoresNum1.clear()
        divisoresNum1.append(int(i))
        
    num1 -= 1






##### num = int(input("Introduce un número: "))
##### 
##### divisoresNum = []
##### totalDivisoresNum = int
##### 
##### esPerfecto = True
##### 
##### while True:
#####     for i in range(1, num):
#####         if num%i == 0:
#####             divisoresNum.append(int(i))
#####             if totalDivisoresNum == num:
#####                 esPerfecto = True
#####                 print(num, "es un número perfecto")
#####             else:
#####                 esPerfecto = False
#####                 print(num, "no es un número perfecto")
#####             totalDivisoresNum = sum(divisoresNum)
#####         else:
#####             divisoresNum = []
#####             pass
##### 
#####         print("La suma de todos los divisores de", num, "es:", totalDivisoresNum, "\n")
#####         num -= 1