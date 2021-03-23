import pytest
from yahtzee import Yahtzee

# These unit tests can be run using the py.test framework
# available from http://pytest.org/

def test_tirar_dados(): # deberia funcionar
        """
        comprueba que la suma de los dados es correcta
        author: Antonio Jose Lojo
        """
        expected = 15
        actual = Yahtzee.tirar_dados(2,3,4,5,1)
        assert expected == actual
        assert 16 == Yahtzee.tirar_dados(3,3,4,5,1)
  

def test_todos_los_numeros_iguales():
        expected = 50
        actual = Yahtzee.todos_los_numeros_iguales([4,4,4,4,4])
        assert expected == actual
        assert 50 == Yahtzee.todos_los_numeros_iguales([6,6,6,6,6])
        assert 0 == Yahtzee.todos_los_numeros_iguales([6,6,6,6,3])
  

def test_suma_solo_unos():
        assert Yahtzee.suma_solo_unos(1,2,3,4,5) == 1
        assert 2 == Yahtzee.suma_solo_unos(1,2,1,4,5)
        assert 0 == Yahtzee.suma_solo_unos(6,2,2,4,5)
        assert 4 == Yahtzee.suma_solo_unos(1,2,1,1,1)


def test_suma_solo_dos():
        assert 4 == Yahtzee.suma_solo_dos(1,2,3,2,6)
        assert 10 == Yahtzee.suma_solo_dos(2,2,2,2,2)


def test_suma_solo_tres():
        assert 6 == Yahtzee.suma_solo_tres(1,2,3,2,3)
        assert 12 == Yahtzee.suma_solo_tres(2,3,3,3,3)
  

def test_suma_solo_cuatros():
        assert 12 == Yahtzee.suma_solo_cuatros(4,4,4,5,5)
        assert 8 == Yahtzee.suma_solo_cuatros(4,4,5,5,5)
        assert 4 == Yahtzee.suma_solo_cuatros(4,5,5,5,5)
  

def test_suma_solo_cincos():
        assert 10 == Yahtzee.suma_solo_cincos(4,4,4,5,5)
        assert 15 == Yahtzee.suma_solo_cincos(4,4,5,5,5)
        assert 20 == Yahtzee.suma_solo_cincos(4,5,5,5,5)
  

def test_suma_solo_seis():
        assert 0 == Yahtzee.suma_solo_seis(4,4,4,5,5)
        assert 6 == Yahtzee.suma_solo_seis(4,4,6,5,5)
        assert 18 == Yahtzee.suma_solo_seis(6,5,6,6,5)
  

def test_par_mas_alto():
        """
        Comprueba que la funcion par mas alto funciona
        """
        # lista6 = [3,4,3,5,6]
        # lista10 = [5,3,3,3,5]
        # lista12 = [5,3,6,6,5]
        assert 6 == Yahtzee.par_mas_alto(3,4,3,5,6)
        # ejercuta
  
def test_par_de_dos():
        assert 16 == Yahtzee.par_de_dos([3,3,5,4,5])
        assert 18 == Yahtzee.par_de_dos([3,3,6,6,6])
        assert 0 == Yahtzee.par_de_dos([3,3,6,5,4])
  

def test_tres_o_cuatro_iguales():
        assert 9 == Yahtzee.tres_o_cuatro_iguales([3,3,3,4,5])
        assert 15 == Yahtzee.tres_o_cuatro_iguales([5,3,5,4,5])
        assert 9 == Yahtzee.tres_o_cuatro_iguales([3,3,3,3,5])

        # break
        assert 12 == Yahtzee.tres_o_cuatro_iguales([3,3,3,3,5])
        assert 20 == Yahtzee.tres_o_cuatro_iguales([5,5,5,4,5])
        assert 12 == Yahtzee.tres_o_cuatro_iguales([3,3,3,3,3])
        assert 0  == Yahtzee.tres_o_cuatro_iguales([3,3,3,2,1])
  

def test_escalera_pequeña():
        assert 15 == Yahtzee.escalera_pequeña([1,2,3,4,5])
        assert 15 == Yahtzee.escalera_pequeña([2,3,4,5,1])
        assert 0 == Yahtzee.escalera_pequeña([1,2,2,4,5])
  

def test_escalera_grande():
        assert 20 == Yahtzee.escalera_grande([6,2,3,4,5])
        assert 20 == Yahtzee.escalera_grande([2,3,4,5,6])
        assert 0 == Yahtzee.escalera_grande([1,2,2,4,5])
  

def test_escalera_completa():
        assert 18 == Yahtzee.escalera_completa([6,2,2,2,6])
        assert 0 == Yahtzee.escalera_completa([2,3,4,5,6])
   
