class Yahtzee:

    def __init__(self, d1, d2, d3, d4, _5):
        """
        Hemos considerado que el primer paso debia ser reordenar el codigo

        author: Antonio Jose
        """
        self.dice = [0]*5
        self.dice[0] = d1
        self.dice[1] = d2
        self.dice[2] = d3
        self.dice[3] = d4
        self.dice[4] = _5

    @staticmethod
    def suma_solo_unos(d1,  d2,  d3,  d4,  d5):
        """
        Esta funcion cuenta los dados que han salido con el número 1. Suma la cantidad de 'unos' y devuelve el resultado.

        author: Jose Rosendo
        """
        s = 0
        for die in [d1, d2, d3, d4, d5]:
            if die == 1:
                s += 1

        return s

    @staticmethod
    def suma_solo_dos(d1,  d2,  d3,  d4,  d5):
        """
        Esta funcion cuenta los dados que han salido con el número 2. Suma la cantidad de 'doses' y devuelve el resultado.

        author: Jose Rosendo
        """
        s = 0
        for die in [d1, d2, d3, d4, d5]:
            if die == 2:
                s += 2

        return s

    @staticmethod
    def suma_solo_tres(d1,  d2,  d3,  d4,  d5):
        """
        Esta funcion cuenta los dados que han salido con el número 3. Suma la cantidad de 'treses' y devuelve el resultado.

        author: Jose Rosendo
        """
        s = 0
        for die in [d1, d2, d3, d4, d5]:
            if die == 3:
                s += 3

        return s

    @staticmethod
    def suma_solo_cuatros(d1,  d2,  d3,  d4,  d5):
        """
        Esta funcion cuenta los dados que han salido con el número 4. Suma la cantidad de 'cuatros' y devuelve el resultado.

        author: Jose Rosendo
        """
        s = 0
        for die in [d1, d2, d3, d4, d5]:
            if die == 4:
                s += 4

        return s

    @staticmethod
    def suma_solo_cincos(d1,  d2,  d3,  d4,  d5):
        """
        Esta funcion cuenta los dados que han salido con el número 5. Suma la cantidad de 'cincos' y devuelve el resultado.

        author: Jose Rosendo
        """
        s = 0
        for die in [d1, d2, d3, d4, d5]:
            if die == 5:
                s += 5

        return s

    @staticmethod
    def suma_solo_seis(d1,  d2,  d3,  d4,  d5):
        """
        Esta funcion cuenta los dados que han salido con el número 6. Suma la cantidad de 'seises' y devuelve el resultado.

        author: Jose Rosendo
        """
        s = 0
        for die in [d1, d2, d3, d4, d5]:
            if die == 6:
                s += 6

        return s

    @staticmethod
    def tirar_dados(d1, d2, d3, d4, d5):
        """
        suma el resultado de todos los dados sin importar el orden
        author: Antonio Jose
        """
        return d1 + d2 + d3 + d4 + d5

        
    @staticmethod
    def todos_los_numeros_iguales(dice):
        """
        Esto lo que hace es ver si todos los dados tienen el mismo nº para darte más puntos
        author: Antonio José
        """
        counts = [0]*(len(dice)+1)
        for die in dice:
            counts[die-1] += 1
        for i in range(len(counts)):
            if counts[i] == 5:
                return 50
        return 0

    @staticmethod
    def crea_lista_dados(self,d1, d2, d3, d4, d5):
        """
        crea una lista de dados que se utiliza en el resto de metodos
        author: Antonio José
        """
        numbers = [0]*6
        numbers[d1-1] += 1
        numbers[d2-1] += 1
        numbers[d3-1] += 1
        numbers[d4-1] += 1
        numbers[d5-1] += 1
        return self.numbers

    @staticmethod
    def par_mas_alto(self, d1, d2, d3, d4, d5):
        """
        Selecciona el par de números más alto que salga en la combinación de dados.
        param: numbers recibe una lista de crea_lista_dados 
        author: Jose Rosendo
        """
        numbers = self.crea_lista_dados(d1, d2, d3, d4, d5)
        
        for number in range(6):
            if (numbers[6-number-1] == 2):
                return (6-number)*2
        return 0

    @staticmethod
    def par_de_dos(numbers):
        """
        Busca si hay pares de dos dados con el mismo dado y anora la suma de estos dados
        param: numbers recibe una lisra de crea_lista_dados
        author: Antonio José Lojo
        """
        n = 0
        score = 0
        for i in range(6):
            if (numbers[6-i-1] >= 2):
                n = n+1
                score += (6-i)
        if (n == 2):
            return score * 2
        return 0

    @staticmethod
    def tres_o_cuatro_iguales(numbers):
        """
        Comprueba si hay tres o 4 dados con el mismo tipo y devuelve la suma de sus valores

        param: numbers lista de crea_lista_dados

        autor: Antonio José Lojo Ojeda
        """
        for i in range(6):
            if (numbers[i] >= 3):
                return (i+1) * 3
            elif (numbers[i] >= 4):
                return (i+1) * 4
        return 0


    @staticmethod
    def escalera_pequeña(numbers):
        """
        Comprueba si existe una escalera pequeña (1,2,3,4,5). Si esto se da, se suman 15 puntos.
        param: numbers lista de crea_lista_dados
        author: Jose Rosendo
        """
        comprobante = True
        for number in numbers:
            if number == 1:
                comprobante = True
            else:
                comprobante = False
                break
        if comprobante:
            return 15
        return 0

    @staticmethod
    def escalera_grande(numbers):
        """
        Comprueba si existe una escalera grande (2,3,4,5,6). Si esto se da, se suman 20 puntos.
        param: numbers lista de crea_lista_dados
        author: Jose Rosendo
        """
        comprobante = True
        for number in numbers[1, 5]:
            if number == 1:
                comprobante = True
            else:
                comprobante = False
                break
        if comprobante:
            return 20
        return 0

    @staticmethod
    def escalera_completa(numbers):
        """
        Comprueba  si hay dos grupos de tres y dos dados iguales, si es así el jugador
        anota la suma de todos los dado 
        """
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        for i in range(6):
            if (numbers[i] == 2):
                _2 = True
                _2_at = i+1
            
            elif (numbers[i] == 3):
                _3 = True
                _3_at = i+1

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0