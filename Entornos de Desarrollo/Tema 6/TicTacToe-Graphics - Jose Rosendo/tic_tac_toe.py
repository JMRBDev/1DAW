import tkinter
import tkinter.font as tkFont
import tkinter.messagebox
import sys

"""Tic Tac Toe game made in Python making use of graphics library Tkinter.

This Tic Tac Toe program is a Multiplayer Offline game.
"""

root = tkinter.Tk()
root.title('Tic-Tac-Toe                 [JMRBDev_]')
#windowIcon = 'src/icon.ico'
#root.iconbitmap(windowIcon)
root.resizable(False, False)

# Colors
bgColor = '#1E1E1E'
buttonColor = '#f5f5f5'
txtColor = '#2d567a'
p1Color = '#ff4545'
p2Color = '#45ff96'

root.config(bg=bgColor, bd=15)
root.geometry('575x650')
fontStyle = tkFont.Font(family='Arial', size=30)
btnFontStyle = tkFont.Font(family='Arial', size=12)

nextP1 = True
movesCount = 0


def centerWindow(window):
    """Centers the main window in the center of the screen canvas

    Args:
        window: Window that will be centered, mainly Tk()
    """
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))


def placeChip(button, playerText):
    """Places the correct chip in the correct cell when a player clicks the desired position

    Args:
    button: Object Button from Tk library, it is the clicked button on which a chip will be placed on
    playerText: Current player indicator. It can be either [Player 1] or [Player 2]
    """
    global nextP1, movesCount, p1Color, p2Color

    if button['text'] == '' and nextP1:
        button['text'] = 'X'
        button['fg'] = p1Color
        playerText['text'] = 'Player 2'
        nextP1 = False
        checkVictory()
        movesCount += 1
    elif button['text'] == '' and not nextP1:
        button['text'] = 'O'
        button['fg'] = p2Color
        playerText['text'] = 'Player 1'
        nextP1 = True
        checkVictory()
        movesCount += 1
    else:
        tkinter.messagebox.showinfo(
            title='Cell already set', message='That cell has already been set, please choose another one.')


def checkVictory():
    """Check if a move is a winning move, if so, the game ends and tell the players who won
    """
    if (button0['text'] == 'X' and button1['text'] == 'X' and button2['text'] == 'X' or
        button3['text'] == 'X' and button4['text'] == 'X' and button5['text'] == 'X' or
        button6['text'] == 'X' and button7['text'] == 'X' and button8['text'] == 'X' or
        button0['text'] == 'X' and button3['text'] == 'X' and button6['text'] == 'X' or
        button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
        button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
        button0['text'] == 'X' and button4['text'] == 'X' and button8['text'] == 'X' or
            button2['text'] == 'X' and button4['text'] == 'X' and button6['text'] == 'X'):
        tkinter.messagebox.showinfo(
            title='The game has ended...', message='Player 1 wins, congratulations!')
        resetGame()

    elif (button0['text'] == 'O' and button1['text'] == 'O' and button2['text'] == 'O' or
          button3['text'] == 'O' and button4['text'] == 'O' and button5['text'] == 'O' or
          button6['text'] == 'O' and button7['text'] == 'O' and button8['text'] == 'O' or
          button0['text'] == 'O' and button3['text'] == 'O' and button6['text'] == 'O' or
          button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
          button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
          button0['text'] == 'O' and button4['text'] == 'O' and button8['text'] == 'O' or
          button2['text'] == 'O' and button4['text'] == 'O' and button6['text'] == 'O'):
        tkinter.messagebox.showinfo(
            title='The game has ended...', message='Player 2 wins, congratulations!')
        resetGame()

    elif movesCount == 8:
        tkinter.messagebox.showinfo(
            title='Tic-Tac-Toe!', message='It is a tie!')
        resetGame()


def resetGame():
    """Reset the game and create a new clean board
    """
    global movesCount, nextP1

    movesCount = 0
    nextP1 = True
    playerText['text'] = 'Player 1'
    button0['text'] = ''
    button1['text'] = ''
    button2['text'] = ''
    button3['text'] = ''
    button4['text'] = ''
    button5['text'] = ''
    button6['text'] = ''
    button7['text'] = ''
    button8['text'] = ''


def closeGame():
    """Close the game and end the python process
    """
    close = tkinter.messagebox.askyesno(
        title='Are you sure?', message='Current match progress will not be saved')
    if close:
        exit()


button0 = tkinter.Button(root, text='', font=fontStyle, bg=buttonColor, fg=txtColor,
                 width=3, height=1, command=lambda: placeChip(button0, playerText))
button0.grid(padx=50, pady=50, row=0, column=0)
button1 = tkinter.Button(root, text='', font=fontStyle, bg=buttonColor, fg=txtColor,
                 width=3, height=1, command=lambda: placeChip(button1, playerText))
button1.grid(padx=50, pady=50, row=0, column=1)
button2 = tkinter.Button(root, text='', font=fontStyle, bg=buttonColor, fg=txtColor,
                 width=3, height=1, command=lambda: placeChip(button2, playerText))
button2.grid(padx=50, pady=50, row=0, column=2)
button3 = tkinter.Button(root, text='', font=fontStyle, bg=buttonColor, fg=txtColor,
                 width=3, height=1, command=lambda: placeChip(button3, playerText))
button3.grid(padx=50, pady=50, row=1, column=0)
button4 = tkinter.Button(root, text='', font=fontStyle, bg=buttonColor, fg=txtColor,
                 width=3, height=1, command=lambda: placeChip(button4, playerText))
button4.grid(padx=50, pady=50, row=1, column=1)
button5 = tkinter.Button(root, text='', font=fontStyle, bg=buttonColor, fg=txtColor,
                 width=3, height=1, command=lambda: placeChip(button5, playerText))
button5.grid(padx=50, pady=50, row=1, column=2)
button6 = tkinter.Button(root, text='', font=fontStyle, bg=buttonColor, fg=txtColor,
                 width=3, height=1, command=lambda: placeChip(button6, playerText))
button6.grid(padx=50, pady=50, row=2, column=0)
button7 = tkinter.Button(root, text='', font=fontStyle, bg=buttonColor, fg=txtColor,
                 width=3, height=1, command=lambda: placeChip(button7, playerText))
button7.grid(padx=50, pady=50, row=2, column=1)
button8 = tkinter.Button(root, text='', font=fontStyle, bg=buttonColor, fg=txtColor,
                 width=3, height=1, command=lambda: placeChip(button8, playerText))
button8.grid(padx=50, pady=50, row=2, column=2)

playerText = tkinter.Label(root, text='Player 1', font=fontStyle,
                   bg=buttonColor, fg=bgColor)
playerText.grid(padx=20, pady=0, row=3, column=1)
resetBtn = tkinter.Button(root, text='Reset', font=btnFontStyle,
                  bg=buttonColor, fg=bgColor, command=lambda: resetGame())
resetBtn.grid(padx=20, pady=0, row=3, column=0)
closeBtn = tkinter.Button(root, text='Close', font=btnFontStyle,
                  bg=buttonColor, fg=bgColor, command=lambda: closeGame())
closeBtn.grid(padx=20, pady=0, row=3, column=2)

centerWindow(root)
tkinter.mainloop()
