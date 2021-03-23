# Usando	como	base	las	clases	desarrolladas	para	gestionar	juegos	de	cartas	(Carta	y	Mazo)	desarrollar	un	juego
# de	cartas	con	las	siguientes	características:
# • Si	el	juego	implica	decisiones	sobre	la	mano,	uno	de	los	jugadores	será humano	y	el	resto	controlados
# por	la	máquina.	No	es	necesario	desarrollar	estrategias	muy	complicadas.
# • Durante	el	juego	es	necesario	imprimir	por	pantalla	la	secuencia	del	juego	para	comprobar	la	corrección
# del	código.
# • No	es	necesario	que	el	juego	sea	muy	complejo	(aunque	se	valorará positivamente),	basta	con	un	simple
# juego	de	la	carta	mayor:	Cada	jugador	saca	una	carta	del	mazo	barajado	comparando	los	valores,	si	hay
# empates	los	jugadores	empatados	vuelven	a	sacar	una	carta	hasta	que	se	deshaga	el	empate.

import random


class Carta:
    palos = ["Bastos", "Copas", "Oros", "Espadas"]
    valores = [None, "As", "Dos", "Tres", "Cuatro", "Cinco",
               "Seis", "Siete", "Ocho", "Nueve", "Sota", "Caballo", "Rey"]

    def __str__(self):  # Capacidad de imprimir el nombre de cada carta
        return f'{self.valor} de {self.palo}'

    def __init__(self, valor=0, palo=0):  # Crear la carta
        self.palo = palo
        self.valor = valor


class Mazo:
    cartas = []

    def baraja_completa(self):
        for palo in Carta.palos:
            for valor in Carta.valores[1:]:
                self.cartas.append(Carta(valor, palo))

    def __str__(self):
        resultado = ""
        for carta in self.cartas:
            resultado += str(carta) + "\n"
        return resultado

    def __init__(self, cartas=None):
        if cartas == None:
            self.baraja_completa()
        else:
            self.cartas = []


class Mano:
    cartasMano = []
    cartaIndex = 0

    def cogerCarta(self, sobrantes):
        if len(sobrantes) > 0:
            cartaARobar = random.randint(0, len(sobrantes) - 1)
            print(len(sobrantes)-1)
            self.cartasMano.append(sobrantes[cartaARobar])
            sobrantes.pop(cartaARobar)
            self.cartaIndex = cartaARobar
            return self.cartasMano
        else:
            return False

    def __init__(self):
        self.cartasMano = []


if __name__ == '__main__':
    baraja = Mazo()  # Crear baraja completa
    contador = 0
    while True:
        if contador == 0:
            print(
                f'La baraja española se compone de las siguientes cartas:\n{baraja}')
            contador += 1

        eleccionP1 = input('[J1] ¿Qué desea hacer? ("Coger", "Salir"): ')
        if eleccionP1.lower() == 'coger':
            manoP1 = Mano()
            cartaEscogidaP1 = manoP1.cogerCarta(baraja.cartas)
            if cartaEscogidaP1:
                print(f'[J1] La carta elegida es: {manoP1.cartasMano[0]}\n')
                eleccionP2 = input(
                    '[J2] ¿Qué desea hacer? ("Coger", "Salir"): ')
            else:
                print('No quedan cartas en la baraja.')
                exit()
            if eleccionP2.lower() == 'coger':
                manoP2 = Mano()
                cartaEscogidaP2 = manoP2.cogerCarta(baraja.cartas)
                if cartaEscogidaP2:
                    print(f'Carta del Jugador 2: {manoP2.cartasMano[0]}\n')
                else:
                    print('No quedan cartas en la baraja.')
                    exit()
                if manoP1.cartaIndex > manoP2.cartaIndex:
                    print('\nEl Jugador 1 gana la partida.\n')
                else:
                    print('\nEl Jugador 2 gana la partida.\n')
            elif eleccionP2.lower() == 'salir':
                print('Saliendo...')
                exit()
            else:
                print('La elección no es válida.\n')
        elif eleccionP1.lower() == 'salir':
            print('Saliendo...')
            exit()
        else:
            print('La elección no es válida.\n')
