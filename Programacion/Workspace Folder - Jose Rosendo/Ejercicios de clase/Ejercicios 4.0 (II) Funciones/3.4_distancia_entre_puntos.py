# Crear una función que calcule la distancia entre dos puntos en el plano.

def distancia(x1, y1, x2, y2):
    distancia_x = abs(x1-x2)
    distancia_y = abs(y1-y2)

    return "La distancia entre los dos puntos es de {} unidades.".format(distancia_x + distancia_y)

print(distancia(10, 20, 7, 35))