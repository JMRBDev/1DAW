import pytest
import math
#import numpy as np
import calculadora

def drange(start,stop,step): 
    i = 0
    r = start 
    while r < stop: 
        i += 1
        r = start + i * step
        yield r

i0=drange(0.0, 1.0, 0.1)

#testdata=[(n,math.sqrt(n)) for n in i0]
testdata = [  (16,4), (4,2)]
#testdata=[(n,math.sqrt(n)) for n in range(1,100)]
#testdata = np.linspace(0,1,11,endpoint=False).tolist()
#testdata=[(n,math.sqrt(n)) for n in range(1,100)]
#testdata=[(1/n,math.sqrt(1/n)) for n in range(1,11)]

# for n in range(1,11):
#     testdata.append((1/n,math.sqrt(1/n)))

@pytest.mark.parametrize("a,expected", testdata)
def test_raiz(a,expected):
    #assert calculadora.raiz(a)==expected
    assert calculadora.raiz(a)==pytest.approx(expected,1e-8)

def test_cuadrado():
    assert calculadora.cuadrado(4)==16

def test_newton_method():
    assert calculadora.newton_method(4)==pytest.approx(2)