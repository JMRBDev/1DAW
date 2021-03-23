# Haz un programa que pida un número y haga una serie de sus sucesores alternando un positivo, un negativo, un positivo, un negativo, etc.

neg = int
num = int(input("Introduce un número: "))
numLista = []

veces = int(input("¿De cuántos números quieres hacer la lista?"))//2

for i in range(veces):
    neg = ((num*-1)-1)
    numLista.append(num)
    numLista.append(neg)
    num += 2

print(numLista)