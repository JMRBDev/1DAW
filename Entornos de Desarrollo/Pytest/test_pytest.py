import calculadora
import math
import pytest

testdata = [(n, math.sqrt(n)) for n in range(1, 101)]


@pytest.mark.parametrize("a,expected", testdata)
def testRaiz(a, expected):
    assert calculadora.raiz(16) == 4
    assert calculadora.raiz(a) == pytest.approx(expected)


def testCuadrado():
    assert calculadora.cuadrado(4) == 16