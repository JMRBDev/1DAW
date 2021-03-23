from dataclasses import dataclass

# Funciones:
    # Ingresar dinero
    # Retirar dinero
    # Ver saldo
    # Establecer / Editar titular
    # Ver titular
    # Cambiar tipo de interés
    # Ver tipo de interés
    # Cambiar saldo mínimo XXXXXX
    # Ver saldo mínimo

@dataclass
class CuentaBancaria:
    titular: str
    numero: str
    saldo: float
    tipoInteres: float
    saldo_minimo: float = 100

def ingresar(cuentaBank, cantIngresar):
    cuentaBank.saldo += cantIngresar
    return cuentaBank

def retirar(cuentaBank, cantRetirar):
    if cantRetirar > cuentaBank.saldo:
        return f"Dispone de {cuentaBank.saldo}, no puede retirar {cantRetirar}."
    elif cuentaBank.saldo - cantRetirar < cuentaBank.saldo_minimo:
        return f"El saldo mínimo debe ser {cuentaBank.saldo_minimo}."
    else:
        cuentaBank.saldo -= cantRetirar
        return cuentaBank

def verSaldo(cuentaBank):
    return cuentaBank.saldo

def cambiarTitular(cuentaBank, nombreTitular):
    cuentaBank.titular = nombreTitular
    return cuentaBank

def verTitular(cuentaBank):
    return cuentaBank.titular

def cambiarTipo(cuentaBank, nuevoInt):
    cuentaBank.tipoInteres = nuevoInt
    return cuentaBank

def verTipo(cuentaBank):
    return cuentaBank.tipoInteres

def cambiarSaldoMin(cuentaBank, nuevoSaldoMin):
    cuentaBank.saldo_minimo = nuevoSaldoMin
    return cuentaBank

def verSaldoMin(cuentaBank):
    return cuentaBank.saldo_minimo

print("Ingresar saldo:")

cc1 = CuentaBancaria("User1", "1234-56789", 100, 0.1, 50)
print(cc1)
cc1 = ingresar(cc1, 400)
print(cc1)

print("\nRetirar saldo:")

cc2 = CuentaBancaria("User2", "1234-12345", 100, 0.1, 50)
print(cc2)
cc2 = retirar(cc2, 60)
print(cc2)

print("\nVer saldo actual:")

cc3 = CuentaBancaria("User3", "1234-98765", 723, 0.1, 50)
print(cc3)
cc3 = verSaldo(cc3)
print("Saldo:", cc3)

print("\nCambiar nombre del titular:")

cc4 = CuentaBancaria("User4", "1234-55526", 1056, 0.1, 50)
print(cc4)
cc4 = cambiarTitular(cc4, "User4Editado")
print("Nuevo titular:", cc4)

print("\nVer nombre del titular:")

cc5 = CuentaBancaria("User5", "1234-111111", 902, 0.1, 50)
print(cc5)
cc5 = verTitular(cc5)
print("Nombre del titular:", cc5)

print("\nCambiar tipo de interés:")

cc6 = CuentaBancaria("User6", "1234-00111", 10042, 0.1, 50)
print(cc6)
cc6 = cambiarTipo(cc6, 0.5)
print(cc6)

print("\nCambiar tipo de interés:")

cc7 = CuentaBancaria("User7", "1234-66557", 134, 0.1, 50)
print(cc7)
cc7 = verTipo(cc7)
print("Tipo de interés:", cc7)

print("\nCambiar saldo mínimo:")

cc8 = CuentaBancaria("User8", "1234-99933", 56, 0.1, 50)
print(cc8)
cc8 = cambiarSaldoMin(cc8, 150)
print(cc8)

print("\nVer saldo mínimo:")

cc9 = CuentaBancaria("User9", "1234-22433", 1956, 0.1, 25)
print(cc9)
cc9 = verSaldoMin(cc9)
print("El saldo mínimo es:", cc9)