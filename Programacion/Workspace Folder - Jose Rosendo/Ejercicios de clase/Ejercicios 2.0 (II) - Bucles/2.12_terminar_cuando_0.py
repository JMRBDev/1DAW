# Haz un programa que pida una seride de números por teclado, y termine cuando se introduzca un 0. Imprime la suma total, cuántos han sido positivos y cuántos negativos.

num = int
numList = []
pos = 0
neg = 0

while True:
    try:
        num = (input("Introduce un número: "))
        print(numList)
        if num == "0":
            print(sum(numList))
            for num in numList:
                if num >= 0:
                    pos += 1
                elif num < 0:
                    neg += 1
            print(pos, neg)
            break 
        elif str == type(num):
            numList.append(int(num))
                
    except ValueError:
        print("ERROR: Introduce un número válido.")