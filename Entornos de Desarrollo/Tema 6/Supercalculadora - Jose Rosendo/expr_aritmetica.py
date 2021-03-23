class ExprAritmetica:
    """Clase que se encarga de la lógica del parser.
    """
    def __es_numero__(self, cadena):
        """Comprueba si un operando es un número o no.

        Args:
            cadena: Carácter que puede ser un número o no.

        Returns:
            bool: True si la cadena es un número entero, False si no lo es.
        """
        try:
            int(cadena)
            return True
        except ValueError:
            return False

    def parse(self, exp):
        """Parsea la expresión a una expresión entendible por el programa.

        Args:
            exp: Expresión que hay que parsear para que sea utilizable.
        
        Returns:
            dict: Diccionario que contiene los operandos y los operadores separados y ordenados
        """
        operandos = []
        operadores = []
        tokens = str.split(exp)
        for token in tokens:
            if self.__es_numero__(token):
                operandos.append(int(token))
            else:
                operadores.append(token)
        return {'Operandos': operandos, 'Operadores': operadores}
