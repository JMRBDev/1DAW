# Crear una función denominada palindromos que reciba una lista de palabras y devuelva una nueva lista con los elementos palíndromos (palabras capicúa, por ejemplo: rallar, eje, reconocer, rajar, salas).

def palindromos(lista):
    palindromosLista = []

    for word in lista:
        if word[::-1] == word:
            palindromosLista.append(word)
        else:
            pass

    return palindromosLista

print(palindromos(["eje", "weaew", "coche", "moto"]))