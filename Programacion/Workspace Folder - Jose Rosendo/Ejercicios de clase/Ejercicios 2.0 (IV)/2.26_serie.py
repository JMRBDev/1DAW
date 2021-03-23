# Dada la siguiente serie: a1=0, a2=1, an=3*an-1+2*an-2 (para n>=3). Calcular el valor y el rango (la n) del primer término mayor o igual a 1000.

a0 = 1  # a1, se va actualizando según la iteración del bucle
a1 = 2  # a2, se va actualizando según la iteración del bucle
contador = 1  # contador de vueltas
n = 0  # posición de a, contador autoincrementado

while n < 1000:
    n = 3 * a1 + 2 * a0  # posición de a según la fórmula de la serie
    a0 = a1  # sustitucion de a0 por a1
    a1 = n  # sustitucion de a1 por la posicion de a
    contador += 1

print("El primer número mayor que 1000 en la serie es", n, "y su lugar es", contador)


# Pseudo-código
# Crear variables para a0 y a1
# Crear contador de vueltas o iteraciones
# Crear n, o posición del contador
# Mientras que n sea menor que 1000,
# La posición de a será igual al resultado de la fórmula
# a1 sustituye a a0 para la próxima iteración
# La posición de a sustituye a a1 para la próxima iteración
# Incrementar el contador en 1
# Imprimir por pantalla el primer número de la serie mayor que 1000 y la posición de a para ese número

