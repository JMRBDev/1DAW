# ¿Cuántas veces se ejecuta el print del siguiente código? ¿Cuál será el resultado por pantalla?
a = 9
for i in range(0,100):
    if 0==a%4 or i%8==0:
        print("a", end=" ")

# Se ejecuta 13 veces, porque solo se ejecuta cuando el resto de a/4 es 0,
# o el resto de la iteración/8 es cero.