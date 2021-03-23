import pytest
from fizz_buzz import *

def test_comprueba_no_numero():
    """
    Comrpueba que no se pueden introducir nombres

    author: Antonio Lojo
    """ 
    n1 = ""
    assert comprobar_numero(n1) == False
    
def test_comprueba_es_numero():
    """ 
    Comrpueba que es un numero

    author: Jose Rosendo
    """
    n1 = 78
    assert comprobar_numero(n1) == True
    
def test_multiplo_3():
    """
    Comprueba que el numero es múltiplo de 3
    
    author: Antonio Lojo
    """
    n1 = 3
    assert fizz(n1) == True

def test_no_es_multiplo_3():
    """
    Comprueba que el numero no es múltiplo de 3
    
    author: Antonio Lojo
    """
    n1 = 7
    assert fizz(n1) == False

def test_multiplo_5():
    """
    Comprueba que el numero es múltiplo de 5
    
    author: Jose Rosendo
    """
    n1 = 5
    assert buzz(n1) == True

def test_no_es_multiplo_5():
    """
    Comprueba que el numero no es múltiplo de 5
    
    author: Jose Rosendo
    """
    n1 = 7
    assert buzz(n1) == False
    
def test_fizz_buzz():
    """
    Comprueba que el numero es múltiplo de 5 y 3
    
    author: Antonio Lojo y Jose Rosendo
    """
    n1 = 15
    assert fizz_buzz(n1) == True

def test_no_fizz_buzz():
    """
    Comprueba que el numero no es múltiplo de 5 y 3
    
    author: Antonio Lojo y Jose Rosendo
    """
    n1 = 16
    assert fizz_buzz(n1) == False