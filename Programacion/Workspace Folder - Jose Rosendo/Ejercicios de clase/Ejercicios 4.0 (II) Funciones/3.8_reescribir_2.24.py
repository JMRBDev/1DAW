fecha_actual = int(input("Fecha actual -- [AÑO]: "))
fecha_nacimiento = int(input("Fecha de nacimiento -- [AÑO]: "))

def esValida ():

        global anos
        anos = 0
        global es_mayor
        es_mayor = True
        es_valida = True
        
        if fecha_actual <= 0 or fecha_nacimiento <= 0:
                es_valida = False
        elif fecha_actual > 0 and fecha_nacimiento > 0:
                anos = fecha_actual-fecha_nacimiento
                es_valida = True

        if es_valida:
                return mayor()
        else:
                return "Los datos introducidos son inválidos."

def mayor():

        if anos < 20:
                es_mayor = False
        elif anos >= 20:
                es_mayor = True

        if es_mayor == True:
                return "Es mayor de 20 años."
        else:
                return "Es menor de 20 años."

print(esValida())