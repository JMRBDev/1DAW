# Calcular la raíz cuadrada sin decimales de un número por aproximación.

variable numero = introduccion numero por teclado

x = numero/2
x2 = x+1

mientras que x sea distinto de x2
    y = numero/x
    x2 = x
    x = (x+y)/2

imprimir: La raíz cuadrada de numero es x