# Crear una función que devuelva si una fecha es válida reutilizando la función del ejercicio 3.6.

def esValida (año):

        es_valida = bool
        if type(año) is not int or año < 0:
                es_valida = False
        elif type(año) is int and año >= 0:
                es_valida = True

        if es_valida:
                return bisiesto(año)
        else:
                return "{} no es un año válido.".format(año)

def bisiesto(año):
    
    es_bisiesto = bool

    if año%4 == 0:
        es_bisiesto = True
    else:
        pass

    if año%100 == 0:
        es_bisiesto = False
    else:
        pass

    if año%400 == 0:
        es_bisiesto = True
    else:
        pass

    if es_bisiesto == True:
        return "El año {} es bisiesto.".format(año)
    else:
        return "El año {} no es bisiesto.".format(año)

print(esValida(2400))