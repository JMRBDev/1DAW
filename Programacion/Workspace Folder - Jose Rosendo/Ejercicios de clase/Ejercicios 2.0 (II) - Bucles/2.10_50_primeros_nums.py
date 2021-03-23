# Muestra los 50 primeros números pares a partir del 0, separados por comas y en orden creciente.

nList = []

for i in range(0,50,2):
    nList.append(i)

print(*nList, sep=", ") # El asterisco (*) desempaqueta la lista y devuelve todos sus elementos sin los corchetes.