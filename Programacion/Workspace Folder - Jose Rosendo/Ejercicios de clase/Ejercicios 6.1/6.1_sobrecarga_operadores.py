# Usando la base desarrollada de la clase Fraccion, completar la sobrecarga de todos los operadores posibles
# usando como referencia el documento “6.A Sobrecarga Operadores.pdf”

class Fraccion:
    numerador = 3
    denominador = 4

    def __init__(self, numerador, denominador=1):
        self.numerador = numerador
        self.denominador = denominador
    
    def __str__(self):
        return '({}, {})'.format(self.numerador, self.denominador)

    def __add__(self, other):
        numerador = self.numerador + other.numerador
        denominador = self.denominador + other.denominador
        return Fraccion(numerador, denominador)

    def __sub__(self, other):
        numerador = self.numerador - other.numerador
        denominador = self.denominador - other.denominador
        return Fraccion(numerador, denominador)

    def __mul__(self, other):
        numerador = self.numerador * other.numerador
        denominador = self.denominador * other.denominador
        return Fraccion(numerador, denominador)
    
    def __floordiv__(self, other):
        numerador = self.numerador // other.numerador
        denominador = self.denominador // other.denominador
        return Fraccion(numerador, denominador)
    
    def __truediv__(self, other):
        numerador = self.numerador / other.numerador
        denominador = self.denominador / other.denominador
        return Fraccion(numerador, denominador)

    def __mod__(self, other):
        numerador = self.numerador % other.numerador
        denominador = self.denominador % other.denominador
        return Fraccion(numerador, denominador)

    def __pow__(self, other):
        numerador = self.numerador ** other.numerador
        denominador = self.denominador ** other.denominador
        return Fraccion(numerador, denominador)

if __name__ == '__main__':
    num = Fraccion(10, 5)
    num1 = Fraccion(2, 3)

    print('SOBRECARGA DE OPERADOR "ADD +": ', num + num1)
    print('SOBRECARGA DE OPERADOR "SUB -": ', num - num1)
    print('SOBRECARGA DE OPERADOR "MUL *": ', num * num1)
    print('SOBRECARGA DE OPERADOR "FLOOR DIV //": ', num // num1)
    print('SOBRECARGA DE OPERADOR "TRUE DIV /": ', num / num1)
    print('SOBRECARGA DE OPERADOR "MOD %": ', num % num1)
    print('SOBRECARGA DE OPERADOR "POW **": ', num ** num1)