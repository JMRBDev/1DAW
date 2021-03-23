# Escribe un programa que solicite una puntuación entre 0.0 y 1.0. Si la puntuación está fuera de ese rango, muestra un mensaje de error. Si la puntuación está entre 0.0 y 1.0, muestra la calificación usando la tabla

puntuaciones = {"Suficiente":"0.6", "Bien":"0.7", "Notable":"0.8", "Sobresaliente":"0.9"}
puntuacion = float(input("Introduce la  puntuación: "))

if puntuacion < 0.0 or puntuacion > 1.0:
    print("Fuera de rango")
else:
    print("\nPuntuación        Calificación\n>= 0.9            Sobresaliente\n>= 0.8            Notable\n>= 0.7            Bien\n>= 0.6            Suficiente\n< 0.6             Insuficiente")
    if puntuacion < 0.6:
        print("Insuficiente")
    elif puntuacion == 0.6:
        print("Suficiente")
    elif puntuacion == 0.7:
        print("Bien")
    elif puntuacion == 0.8:
        print("Notable")
    elif puntuacion >= 0.9:
        print("Sobresaliente")
    else:
        pass