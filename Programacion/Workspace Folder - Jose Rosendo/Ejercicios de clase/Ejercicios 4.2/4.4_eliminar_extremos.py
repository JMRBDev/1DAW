# Crear una función denominada eliminar_extremos que reciba una lista y elimine el primer y el último elemento de la misma. Usar la función para crear un programa que calcule la puntuación media de la valoración de 8 jueces eliminando los valores máximo y mínimo.

def eliminar_extremos(notas):
    try:
        if len(notas) == 8:
            notas.sort()
            return sum(notas[1:-1])/8
        else:
            return "La cantidad de notas introducidas debe ser 8."
    except:
        return "Introduzca las notas de los 8 jueces correctamente."

print(eliminar_extremos([6,4,5,3,1,3,6,9]))