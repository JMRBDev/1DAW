# Haz el programa del ejercicio anterior, pero muestra también el máx y min de los números

num = int
numList = []

while True:
    try:
        num = (input("Introduce un número: "))
        print(numList)
        if num == "fin":
            print("Suma total:", sum(numList), "\nCantidad de números:", len(numList), "\nMedia:", sum(numList)/len(numList), "\nMáximo", max(numList), "\nMinimo", min(numList))
            break 
        elif str == type(num):
            numList.append(int(num))
                
    except ValueError:
        print("ERROR: Introduce un número válido.")