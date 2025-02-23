import random
from tkinter import Tk, Label, Button, Frame

player = "X" 

def next_turn(row, column):
    global player

    if buttons[row][column]["text"] == "" and check_winner() is False:
        buttons[row][column]["text"] = player 

        if check_winner():
            label.config(text=(player + " wins"))
            update_score(player) 
        elif empty_spaces() is False:
            label.config(text="It's a draw")
        else:
            player = "O"  
            label.config(text=(player + " turn"))
            ai_turn()  

def ai_turn():
    global player 

    if empty_spaces() and check_winner() is False:
        row, column = random.choice(get_empty_spaces())
        buttons[row][column]["text"] = player  

        if check_winner():
            label.config(text=(player + " wins"))
            update_score(player)  
        elif empty_spaces() is False:
            label.config(text="It's a draw")
        else:
            player = "X"  
            label.config(text=(player + " turn"))

def get_empty_spaces():
    empty = []
    for row in range(3):
        for col in range(3):
            if buttons[row][col]["text"] == "":
                empty.append((row, col))  
    return empty

def check_winner():
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            return True

    for col in range(3):
        if buttons[0][col]["text"] == buttons[1][col]["text"] == buttons[2][col]["text"] != "":
            return True

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True

    return False

def empty_spaces():
    for row in range(3):
        for col in range(3):
            if buttons[row][col]["text"] == "":
                return True
    return False

def new_game():
    global player 
    player = "X"  
    label.config(text=player + " turn")
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="")
    update_score_display()  

def update_score(winner):
    if winner == "X":
        scores["X"] += 1
    else:
        scores["O"] += 1
    update_score_display()

def update_score_display():
    score_label.config(text=f"X: {scores['X']} - O: {scores['O']}")

window = Tk()
window.title("Tic-Tac-Toe")

scores = {"X": 0, "O": 0}

buttons = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

score_label = Label(text="X: 0 - O: 0", font=('consolas', 20))
score_label.pack(side="top")

label = Label(text="X turn", font=('consolas', 40))
label.pack(side="top")

reset_button = Button(text="Restart", font=('consolas', 20), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('consolas', 40), width=5, height=2,
                                      command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

window.mainloop()