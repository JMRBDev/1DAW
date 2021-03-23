import random
import sys
import socket
import time

def game_rules():
    print (""" 
      Bienvenido/a al juego 3 en Raya...
      Elige un equipo para jugar (X / O). Tu ordenador jugará solo
      contra el otro ordenador que esté jugando en el mismo puerto.
      El tablero de juego será el siguiente:
                             1 | 2 | 3            
                            -----------
                             4 | 5 | 6            
                            -----------
                             7 | 8 | 9
      Si quieres salir o jugar de nuevo, introduce (q or Q).
      El juego va a empezar...
      """)


def game_setup():
    human = input("\n¿Qué ficha quieres ser? (X or O)\n")
    while human not in ('x','X','o','O'):
        print ("Ficha inválida, inténtalo de nuevo.")
        human = input("¿Qué ficha quieres ser? (X or O)\n")
        
    human = human.upper()
    if human == 'X':
        machine = 'O'
    else:
        machine = 'X'
        
    print ("Okay, eres %s." % human)
    draw_board(range(1,10))
    
    if human.lower() == 'x':
        turn = False
        print ("Jose empieza\n")
    else: 
        turn = True
        print ("Antonio empieza\n")
        
    return human, machine, turn


def draw_board(values):
    print ("\n\t", values[0], "|", values[1], "|", values[2])
    print (" " * 6, "-" * 11)
    print ("\t", values[3], "|", values[4], "|", values[5])
    print (" " * 6, "-" * 11)
    print ("\t", values[6], "|", values[7], "|", values[8], "\n")


def win_conditions(human, machine, values):
    wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for v in wins:
        if values[v[0]] == values[v[1]] == values[v[2]] != ' ':
            winner = values[v[0]]
            if winner == human:
                return 'H'
            elif winner == machine:
                return 'M'

    if ' ' not in values:
        return 'T'


def human_move(values): 
    c1_aux = [str(x) for x in s.recv(1024).decode()]
    print('Movimiento de Jose: ', *c1_aux)
    c1 = c1_aux[0]
    return (int(c1) - 1)

    play_again()


def machine_move(human, machine, values):
    best_move = [0, 2, 4, 6, 8]
    empty_places = []
    best_move_left = []
    
    for i in range(0,9):
        if values[i] == " ":
            empty_places.append(i)
            
    for p in empty_places:
        values[p] = machine
        if win_conditions(human, machine, values) == "M":
            return p
        values[p] = " "
        
    for p in empty_places:
        values[p] = human
        if win_conditions(human, machine, values) == "H":
            return p
        values[p] = " "
        
    for m in best_move:
        if m in empty_places:
            best_move_left.append(m)      
    if len(best_move_left) != 0:
        return best_move_left[random.randrange(len(best_move_left))]

    return empty_places[random.randrange(len(empty_places))]


def play(human, machine, turn, values): 
    while win_conditions(human, machine, values) == None:
        if turn:
            time.sleep(random.uniform(1, 2))
            m_move = machine_move(human, machine, values)
            s.send(str(m_move+1).encode())
            print ("Movimiento de Antonio:", (m_move + 1))
            values[m_move] = machine
        else:
            time.sleep(random.uniform(1, 2))
            h_move = human_move(values)
            values[h_move] = human
            
        draw_board(values)
        turn = not turn
        
    return win_conditions(human, machine, values)


def play_again():
    print ("\nSi quieres jugar de nuevo, presiona (r or R).")
    c = input("Si quieres salir, presiona (ENTER): ")
    if c == 'r' or c == 'R':
        main() 
    else:
        print ("Gracias por jugar. Saliendo...")
        sys.exit(0)

  
def main():
    players = game_setup()
    human = players[0]
    machine = players[1]
    turn = players[2]
    values = [' '] * 9
    
    state = play(human, machine, turn, values)
    if state == "H":
        print ("Has ganado la partida. ¡Felicidades!")
    elif state == "M":
        print ("¡Tu adversario ha ganado la partida!")
    else:
        print ("¡Ha habido un empate!")

    play_again()


if __name__ == '__main__':
    port = 12345
    s = socket.socket()

    s.connect(('192.168.12.106', port))

    game_rules()
    main()