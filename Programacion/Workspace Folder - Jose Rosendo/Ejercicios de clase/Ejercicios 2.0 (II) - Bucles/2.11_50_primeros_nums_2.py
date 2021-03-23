# Haz el programa anterior mostrando también la suma de todos los números

nList = []

for i in range(0,50,2):
    nList.append(i)

print(*nList, sep=", ") # El asterisco (*) desempaqueta la lista y devuelve todos sus elementos sin los corchetes.
print(sum(nList))