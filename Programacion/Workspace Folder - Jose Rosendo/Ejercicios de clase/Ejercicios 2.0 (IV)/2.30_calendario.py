# Dado un mes del año y el día de la semana en que comienza, mostrar por pantalla una representación del calendario similar a la muestra.

dia = input("Introduce un día: ")
mes = input("Introduce un mes: ")

# Averigua el número de días en el mes
if mes in ["Enero", "Marzo", "Mayo", "Julio", "Agosto", "Octubre", "Diciembre"]:
    numDias = 31
elif mes in ["Febrero"]:
    numDias = 28
else:
    numDias = 30

# Espacios en blanco antes del día 1
diasSemana = ["L", "M", "X", "J", "V", "S", "D"]
posicion = diasSemana.index(dia)

print(mes)
print(" L  M  X  J  V  S  D")

# Imprimir los espacios en blanco cuando el día 1 no sea Lunes
for i in range(posicion):
    print("  ", end=" ")
# Imprimir días
for i in range(numDias):
    print("%2d" % (i+1), end=" ")
    # Si el día es Domingo, saltar a la siguiente línea
    if (i + posicion) % 7 == 6:
        print()



#Pseudocódigo
#Pedir día en que comienza el mes y el mes en cuestión
#Si el mes es uno de los que tienen 31 dias, establecer el nº de dias en 31, si es febrero se establece en 28 y si es cualquier otro, en 31
#Listar los dias de la semana
#Establecer la posición de inicio con index
#Imprimir nombre del mes y los dias de la semana
#Para todos los puestos en la posición del inicio de la semana imprimir un hueco en blanco
#Para cada dia del mes imprimir un numero hasta el final del mes previamente establecido
#Si la posicion es Domingo (día 7), saltar de línea