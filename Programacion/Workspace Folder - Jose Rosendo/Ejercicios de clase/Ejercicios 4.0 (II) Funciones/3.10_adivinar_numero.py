# Crear un programa para jugar a adivinar un número entre 0 y 100. Debe ofrecer cinco oportunidades e indicar ante un fallo si el objetivo es menor, mayor o esta muy cerca (a 2 de distancia o menos). Se debe utilizar una función para comprobar si el número es el acertado o no y hacer las indicaciones al jugador.

import random

intentos = 0
numero = random.randint(0, 100)


def adivinar():
    global numero
    global intentos

    while intentos < 5:
        for i in range(5):
            guess = int(input("Introduce un número: "))
            if guess == numero:
                break
            elif guess < numero and guess + 1 != numero and guess + 2 != numero:
                if intentos == 4:
                    break
                else:
                    print("¡Más arriba!")
            elif guess > numero and guess - 1 != numero and guess - 2 != numero:
                if intentos == 4:
                    break
                else:
                    print("¡Más abajo!")
            elif guess + 1 == numero or guess - 1 == numero:
                if intentos == 4:
                    break
                else:
                    print("¡A uno!")
            elif guess + 2 == numero or guess - 2 == numero:
                if intentos == 4:
                    break
                else:
                    print("¡A dos!")

            intentos += 1
        break

    if intentos <= 4 and guess == numero:
        return "\n¡Has ganado!"
    else:
        return "\n¡Has perdido! Suerte la próxima vez."


print(adivinar())
