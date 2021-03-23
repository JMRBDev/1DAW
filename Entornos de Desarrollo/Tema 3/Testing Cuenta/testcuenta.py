from cuenta1 import *
import pytest
import random

def testIngresar():
    cuenta1 = CuentaBancaria('Jose', '656646', 300, 0.3, 50)
    saldoInicial = verSaldo(cuenta1)
    cuenta1 = ingresar(cuenta1, 20)

    assert saldoInicial + 20 == verSaldo(cuenta1)

cant_inicial = [random.randint(100,5000) for i in range(100)]
a_ingresar = [random.randint(100,5000) for i in range(100)]
testdata = [(cant_inicial[i], a_ingresar[i], cant_inicial[i] + a_ingresar[i]) for i in range(len(cant_inicial))]

@pytest.mark.parametrize('cant_inicial,entrada,res_esperado', testdata)
def testRetirar(cant_inicial, entrada, res_esperado):
    cuenta1 = CuentaBancaria('Jose', '656646', 300, 0.3, 50)
    saldoInicial = verSaldo(cuenta1)
    cuenta1 = retirar(cuenta1, 120)

    #assert saldoInicial - 120 == verSaldo(cuenta1)
    #assert saldoInicial - 120 > verSaldoMin(cuenta1)

    assert saldoInicial - entrada == res_esperado