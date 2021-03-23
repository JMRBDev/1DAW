from typing import Union
from math import sqrt

def raiz(x:Union[int,float]) -> Union[int,float]:
    r = x
    t = 0
    while (t!=r):
       t = r
       r = 0.5 * ( (x/r) + r)
    return r

def cuadrado(x: Union[int,float]) -> Union[int,float]:
    return x*x

def newton_method(number, number_iters=500):
    a = float(number)  # number to get square root of
    for i in range(number_iters):  # iteration number
        number = 0.5 * (number + a / number)  # update
        # x_(n+1) = 0.5 * (x_n +a / x_n)
    return number

print(raiz(4.1))
print(sqrt(4.1))
print(newton_method(4.1))
