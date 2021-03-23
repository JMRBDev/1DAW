# Jose Rosendo y Antonio Manzano

import random
import sys
import socket
import time

def game_rules():
    print (""" 
      Bienvenido al tres en raya.
      Veras como ambas maquina juegan entre si.
      Los movimientos que verás se representan en el tablero de la siguiente manera:
                             1 | 2 | 3            
                            -----------
                             4 | 5 | 6            
                            -----------
                             7 | 8 | 9
      Para salir del juego presiona "q" o "Q".

      """)


def game_setup():
    human = input("\n¿Que ficha quieres ser? (X or O)\n")
    while human not in ('x','X','o','O'):
        print ("Ficha inválida.")
        human = input("¿Que ficha quieres ser? (X or O)\n")
        
    human = human.upper()
    if human == 'X':
        machine = 'O'
    else:
        machine = 'X'
        
    print ("Vale, ",human, " es tuya.")
    draw_board(range(1,10))
    
    # randomly decide who will play first
    
    if human.lower()=="x":
        turn= False
        print ("Empiezo yo\n")
    else: 
        print ("Empieza Jose\n")
        turn= True
    return human, machine, turn


def draw_board(values):
    print ("\n\t", values[0], "|", values[1], "|", values[2])
    print (" " * 6, "-" * 11)
    print ("\t", values[3], "|", values[4], "|", values[5])
    print (" " * 6, "-" * 11)
    print ("\t", values[6], "|", values[7], "|", values[8], "\n")


def win_conditions(human, machine, values):
    # wins list contain all the winning conditions to check
    wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for v in wins:
        if values[v[0]] == values[v[1]] == values[v[2]] != ' ':
            winner = values[v[0]]
            if winner == human:
                return 'H'
            elif winner == machine:
                return 'M'
                
    if ' ' not in values: 
        return 'T'  # Tie game


def human_move(values): 
    # get the human input for next move
    global c
    c1_aux = [str(x) for x in c.recv(1024).decode()]
    print("Movimiento de Antonio: ",*c1_aux)
    c1 = c1_aux[0]

    return (int(c1) - 1)
            
    # if player quit, ask if she/he wants to play a new game
    play_again()
def machine_move(human, machine, values):
    best_move = [0, 2, 4, 6, 8]
    empty_places = []
    best_move_left = []
    
    # create the list of possible moves
    for i in range(0,9):
        if values[i] == " ":
            empty_places.append(i)
            
    # check if computer can win with a choice for next move
    for p in empty_places:
        values[p] = machine
        if win_conditions(human, machine, values) == "M":
            return p
        values[p] = " "
        
    # check if human can win with the next move to block it
    for p in empty_places:
        values[p] = human
        if win_conditions(human, machine, values) == "H":
            return p
        values[p] = " "
        
    # try one of the best move left to increase odds of winning
    for m in best_move:
        if m in empty_places:
            best_move_left.append(m)      
    if len(best_move_left) != 0:
        return best_move_left[random.randrange(len(best_move_left))]
        
    # if none of the above possibilities, pick a random spot left
    return empty_places[random.randrange(len(empty_places))]


def play(human, machine, turn, values): 
    while win_conditions(human, machine, values) == None:
        # check & change "turn" variable to see whose turn is to move
        if turn:
            time.sleep(random.uniform(1,2))
            m_move = machine_move(human, machine, values)
            c.send(str(m_move+1).encode())

            print ("Movimiento de Jose:", (m_move + 1))
            values[m_move] = machine        
        else:
            time.sleep(random.uniform(1,2))
            h_move = human_move(values)
            values[h_move] = human
            
        draw_board(values)
        turn = not turn
        
    return win_conditions(human, machine, values)


def play_again():
    # play a new game or exit
    print ("\nSi quieres repetir pulsa R")
    c = input("Si no, pulsa enter para salir: ")
    if c == 'r' or c == 'R':
        main() 
    else:
        print ("Thanks for playing. Bye...")
        sys.exit(0)

  
def main():

    # setup human & computer markers and order of playing
    players = game_setup()
    human = players[0]
    machine = players[1]
    turn = players[2]
    values = [' '] * 9
    
    # check who won the game
    state = play(human, machine, turn, values)
    if state == "H":
        print ("Ha ganado Jose.")
    elif state == "M":
        print ("¡He ganado!")
    else:
        print ("Empate")
        
    # ask player if she/he wants to play a new game
    play_again()


if __name__ == '__main__':

    s = socket.socket()  
    print ("Socket successfully created")
    port = 12345
    s.bind(('', port))
    print ("socket binded to %s" %(port))
    s.listen(5)
    c, addr = s.accept()
    print ('Got connection from', addr)
    game_rules()
    main()