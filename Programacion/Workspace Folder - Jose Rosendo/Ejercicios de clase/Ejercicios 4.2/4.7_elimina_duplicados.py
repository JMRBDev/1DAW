# Crear una función denominada elimina_duplicados que reciba una lista y la ordene eliminando los duplicados. Debe devolver una nueva lista con los elementos que se han eliminado.

def elimina_duplicados(lista):
    eliminados = []
    for item in lista:
        if lista.count(item) == 1:
            pass
        else:
            eliminados.append(item)
            lista.pop(item)
    
    return "La lista es: {} y los eliminados son: {}".format(sorted(lista), eliminados)

print(elimina_duplicados([1,1,1,4,5,3,3,8,7,6]))