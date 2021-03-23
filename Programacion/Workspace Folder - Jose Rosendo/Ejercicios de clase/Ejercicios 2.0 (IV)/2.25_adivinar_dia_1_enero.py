# Introducir una fecha por teclado y el día de la semana del 1 de enero de ese año y calcular el día de la semana correspondiente a la fecha introducida.

fecha_actual = int(input("Fecha actual -- [DÍA]: ")), input("Fecha actual -- [MES]: "), int(input("Fecha actual -- [AÑO]: "))
dia_uno_enero = input("¿Qué día fue el 1 de Enero de ese mismo año? ")

dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
dias_semana2 = []

dias = 0 #Contador de días totales

while True:
    if fecha_actual[1].lower() != "enero":
        dias += 31
    elif fecha_actual[1].lower() == "enero":
        dias += fecha_actual[0]
        break

    if fecha_actual[1].lower() != "febrero":
        dias += 28
    elif fecha_actual[1].lower() == "febrero":
        dias += fecha_actual[0]
        break

    if fecha_actual[1].lower() != "marzo":
        dias += 31
    elif fecha_actual[1].lower() == "marzo":
        dias += fecha_actual[0]
        break

    if fecha_actual[1].lower() != "abril":
        dias += 30
    elif fecha_actual[1].lower() == "abril":
        dias += fecha_actual[0]
        break

    if fecha_actual[1].lower() != "mayo":
        dias += 31
    elif fecha_actual[1].lower() == "mayo":
        dias += fecha_actual[0]
        break

    if fecha_actual[1].lower() != "junio":
        dias += 30
    elif fecha_actual[1].lower() == "junio":
        dias += fecha_actual[0]
        break

    if fecha_actual[1].lower() != "julio":
        dias += 31
    elif fecha_actual[1].lower() == "julio":
        dias += fecha_actual[0]
        break

    if fecha_actual[1].lower() != "agosto":
        dias += 31
    elif fecha_actual[1].lower() == "agosto":
        dias += fecha_actual[0]
        break

    if fecha_actual[1].lower() != "septiembre":
        dias += 30
    elif fecha_actual[1].lower() == "septiembre":
        dias += fecha_actual[0]
        break

    if fecha_actual[1].lower() != "octubre":
        dias += 31
    elif fecha_actual[1].lower() == "octubre":
        dias += fecha_actual[0]
        break

    if fecha_actual[1].lower() != "noviembre":
        dias += 30
    elif fecha_actual[1].lower() == "noviembre":
        dias += fecha_actual[0]
        break

    if fecha_actual[1].lower() != "diciembre":
        dias += 31
    elif fecha_actual[1].lower() == "diciembre":
        dias += fecha_actual[0]
        break
 
for i in range(dias+1):
    mod = i%7
    dias_semana2.append(dias_semana[mod])

print("El día", end=" ")
print(fecha_actual[0], "/", fecha_actual[1].capitalize(), "/", fecha_actual[2], sep="", end=" ")
print("cae en ", dias_semana2[-1], ".", sep="")




#Pseudo-código
#Pedir fecha actual
#Pedir dia 1 de enero
#Establecer variable con la lista de los dias de la semana, y una lista vacia
#Hacer contador de dias
#Bucle para comparar los meses y los días con la fecha actual
#Si el mes no coincide con el mes de la iteracion, suma al contador de dias el nº de dias 
#En cambio, si el mes coincide con el mes de la iteracion, suma al contador de dias el día actual
#Recorre la lista de dias de la semana tantas veces como dias totales hayan en mi fecha actual
#Imprime por pantalla el último elemento de la lista de días de la semana que coincide con el dia de la fecha actual