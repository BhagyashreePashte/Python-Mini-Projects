
import tkinter as tk
from tkinter import messagebox

# Function to check for a winner or draw
def check_winner():
    for combo in [[0,1,2], [3,4,5], [6,7,8], 
                  [0,3,6], [1,4,7], [2,5,8],
                  [0,4,8], [2,4,6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "": 
            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="green")
            buttons[combo[2]].config(bg="green")
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]["text"]} Wins!")
            root.quit()
            reset_game()
            return
        
        # Check for draw
    if all(button["text"] != "" for button in buttons):
        messagebox.showinfo("Game Over", "It's a draw!")
        reset_game()

# Function to handle button clicks
def button_click(index):
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        check_winner()
        toggle_player()

# Function to reset the game
def reset_game():
    global current_player
    current_player = "X"
    for button in buttons:
        button["text"] = ""

def toggle_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"
    label.config(text=f"Player {current_player}'s turn")

# Initialize main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

buttons = [tk.Button(root, text="", font=("normal",25), width=6, height=2, command=lambda i=i: button_click(i)) for i in range(9)]

# Create 3x3 grid of buttons
for i,button in enumerate(buttons):
    button.grid(row=i //3, column=i % 3)

# Game variables
current_player = "X"
winner = False
label = tk.Label(root,  text=f"Player {current_player}'s turn ", font=("normal", 16))
label.grid(row=3, column=0, columnspan= 3)


# Run the application
root.mainloop()