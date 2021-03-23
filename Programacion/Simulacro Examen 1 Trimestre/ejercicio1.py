import random

def numero_aleatorio():
    numero = str(random.randrange(10000,99999))
    return numero

def comprueba(numero, guess):
    intentos = 1
    heridos = []
    muertos = []
    print(numero)

    if numero == guess:
        return "Has ganado en {} intentos.".format(intentos)

    for i in range(len(guess)):
        if i in list(numero):
            heridos.append(i)
        if i == list(numero[i]):
            muertos.append([i])

    return "{} heridos y {} muertos.".format(heridos, muertos)

while True:
    guess = input("Introduce un número de 5 cifras: ")
    if len(guess) == 5:
        print(comprueba(numero_aleatorio(), guess))
    else:
        print("El número debe tener 5 cifras.")