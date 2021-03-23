# Haz un programa que lea números repetidamente hasta que el usuario escriba "fin". Cuando lo haga, muestra la suma de todos los números, la cantidad de números y la media de esos números. Si el usuario introduce algo distinto de un nº o "fin", muestra un error y pasa al número siguiente.

num = int
numList = []

while True:
    try:
        num = (input("Introduce un número: "))
        print(numList)
        if num == "fin":
            print(sum(numList), len(numList), sum(numList)/len(numList))
            break 
        elif str == type(num):
            numList.append(int(num))
                
    except ValueError:
        print("ERROR: Introduce un número válido.")