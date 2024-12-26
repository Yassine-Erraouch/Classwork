import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from PIL import Image, ImageTk
from random import choice

#----------------------------------------functions--------------------------------------
player = choice(["X", "O"])
current_player = player
#creating the scores
score_x = 0
score_o = 0
def change_player():
    global current_player
    if current_player == "X":
        button.configure(image=x_img)
        current_player = "O"
    else:
        button.configure(image=o_img)
        current_player = "X"

def new_game():
    global player, current_player
    player = choice(["X", "O"])
    current_player = player

def reset_game():
    global player, current_player
    player = choice(["X", "O"])
    current_player = player


#---------------------------------------------------------------------------------------

#windows creation
window= ttk.Window()
window.title("Tic Tac Toe")
window.geometry("400x400")
style = ttk.Style("minty")


#---------------------------------------widgets-----------------------------------------

#creating the frames

score_frame = ttk.Frame(window)
score_frame.pack(side=TOP)

board_frame = ttk.Frame(window)
board_frame.pack(side=TOP)

buttons_frame = ttk.Frame(window)
buttons_frame.pack(side=BOTTOM)


#creating the images
x_img = ImageTk.PhotoImage(Image.open(r"Python\TKinter\Tkinter_Practice\src\x.png").resize((50, 50)))
o_img = ImageTk.PhotoImage(Image.open(r"Python\TKinter\Tkinter_Practice\src\o.png").resize((50, 50)))

#creating the buttons grid

for i in range(9):
    button = ttk.Button(board_frame, text="", width=10, command= change_player)
    button.grid(row=(i // 3) + 1, column=i % 3)



label_score = ttk.Label(score_frame, text=f"Score - X: {score_x} | O: {score_o}", font=("Arial", 14))
label_score.grid(row=0, column=0, columnspan=3)

#creating the new games and reset buttons
button_new_game = ttk.Button(buttons_frame, text="New Game", width=10, command=new_game)
button_new_game.grid(row=4, column=0)

button_reset = ttk.Button(buttons_frame, text="Reset", width=10, command=reset_game)
button_reset.grid(row=4, column=1)

#-------------------------------------------------mainloop--------------------------------------
window.mainloop()