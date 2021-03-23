# El juego del ahorcado

import random

def juego():

    palabras = ["cerillas", "patrulla", "papel", "azor", "alerones", "conversar", "sollozo", "manzana"]
    palabra = random.choice(palabras)
    palabra_lista = list(palabra)

    secreto = []

    intento = 10

    for i in range(len(palabra_lista)):
        secreto.append("_")

    print(*secreto)
    ### print(palabra) #DEBUG ONLY

    cantidad = 0

    while secreto != palabra_lista:
        if intento < 1:
            break

        for i in range(intento):

            for j in palabra_lista:
                guess = input("Introduce una letra: ")

                for k in palabra_lista:
                    if guess != k:
                        pass
                    else:
                        cantidad += 1

                if cantidad > 0:
                    print("Bien, hay", cantidad, guess)
                    print("Quedan", intento-1, "intentos.\n")
                    for l in range(len(palabra_lista)):
                        if guess == palabra_lista[l]:
                            secreto[l] = guess
                    print(*secreto)
                else:
                    print("Oops, fallo.")
                    print("Quedan", intento-1, "intentos.\n")
                    print(*secreto)

                cantidad = 0
                intento -= 1
                break
            break

    if secreto != palabra_lista:
        print("\nHas perdido. ¡Suerte la próxima vez!", "Siguiente partida:", sep="\n\n\n\n")
    else:
        print("\n¡VICTORIA!", "Siguiente partida:", sep="\n\n\n\n")


while True:
    juego()