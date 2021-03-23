# Di si el año es bisiesto o no

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

print(bisiesto(2400))