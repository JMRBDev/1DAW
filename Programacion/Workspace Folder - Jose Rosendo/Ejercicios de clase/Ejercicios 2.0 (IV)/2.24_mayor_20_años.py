# Introducir por teclado la fecha actual y la fecha de nacimiento del usuario (día, mes y año) e indicar si es mayor de 20 años.

fecha_actual = int(input("Fecha actual -- [DÍA]: ")), int(input("Fecha actual -- [MES]: ")), int(input("Fecha actual -- [AÑO]: "))
fecha_nacimiento = int(input("Fecha de nacimiento -- [DÍA]: ")), int(input("Fecha de nacimiento -- [MES]: ")), int(input("Fecha de nacimiento -- [AÑO]: "))

anos = (fecha_actual[2]-fecha_nacimiento[2])

if anos < 20:
    print("Es menor de 20 años.")
elif anos >= 20:
    print("Es mayor de 20 años, o tiene 20 años.")


# Pseudo-código:
# Pedir fecha actual
# Pedir fecha nacimiento
# Calcular años restando f_actual menos f_nacimiento
# Si años es menor que 20,
#   Imprimir por pantalla que es menor que 20
# En otro caso si años es mayor o igual que 20,
#   Imprimir por pantalla que es mayor que 20, o igual