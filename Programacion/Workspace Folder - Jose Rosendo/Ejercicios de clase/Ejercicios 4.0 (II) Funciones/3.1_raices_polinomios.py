# Crear un programa que calcule las raíces de un polinomio de segundo grado del tipo: ax2 + bx +c

from math import sqrt

def raices(a, b, c):

    discriminante = (b**2)-4*a*c

    if discriminante >= 0:
        raiz_1=(-b+sqrt(discriminante))/2*a
        raiz_2=(-b-sqrt(discriminante))/2*a
    else:
        raiz_1= complex((-b/(2*a)),sqrt(-discriminante)/(2*a))
        raiz_1= complex((-b/(2*a)),-sqrt(-discriminante)/(2*a))

    if discriminante > 0:
        print("El polinomio tiene dos raíces: ", raiz_1, "y", raiz_2)
    elif discriminante == 0:
        print("El polinimio tiene una raíz: ", raiz_1)
    else:
        print("El polinomio tiene dos raíces: ", raiz_1, "y", raiz_2)

raices(3, -5, 1)