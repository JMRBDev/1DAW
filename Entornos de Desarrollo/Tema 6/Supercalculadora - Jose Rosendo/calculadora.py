"""Calculadora básica que solo suma, resta y divide.
"""


class Calculadora:
    """Esta es la clase principal del programa.
    """
    def sumar(self, a, b):
        """Función que agrega un número a otro.

        Args:
            a: Primer sumando.
            b: Segundo sumando.
        
        Returns:
            a y b agregados entre sí (suma).
        """
        return a + b

    def restar(self, a, b):
        """Función que sustrae un número a otro.

        Args:
            a: Minuendo.
            b: Sustraendo.
        
        Returns:
            b sustraído de a (diferencia).
        """
        return a - b

    def dividir(self, a, b):
        """Función que divide un número entre otro.

        Args:
            a: Dividendo.
            b: Divisor.

        Returns:
            Cociente de la división entre a y b.
        """
        if b == 0:
            return ZeroDivisionError
        if a % b != 0:
            return ValueError
        else:
            return a // b  # En Python 2.x esto funciona sin problemas, pero en Python 3, no. ¿Sabes arreglarlo?
