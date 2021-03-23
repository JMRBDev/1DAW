# Crear una función denominada en_orden_ascendente que reciba una lista y devuelva True si se encuentra ordenada en orden ascendente o False si no es así. Crear otra función denominada esta_ordenada que reciba también una lista y devuelva True si se encuentra ordenada (ascendente o descendente) y False si no es así. Intenta hacerlo sin tener que recorrer la lista dos veces.

def en_orden_ascendente(lista):
    ordenada = sorted(lista)
    if lista == ordenada:
        return True
    else:
        return False

def esta_ordenada(lista):
    ordenada1, ordenada2 = sorted(lista), sorted(lista, reverse=True)
    if lista == ordenada1 or lista == ordenada2:
        return True
    else:
        return False

print(en_orden_ascendente([1,2,3,4,5]), esta_ordenada([5,4,3,2,1]))