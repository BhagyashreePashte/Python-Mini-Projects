"""
WORKFLOW OF PROJECT:
1- Input from user(Rock, Psaper,  Scissor)
2- Computer choice (Computer will choose randomly not conditionally)
3- Result Print

Cases:
A - Rock
Rock - Rock = tie ✅
Rock - Paper = Paper Win ✅
Rock - Scissor = Rock Win ✅

B - Paper
Paper - Paper = tie ✅
Paper - Rock =  Paper Win ✅
Paper - Scissor = Scissor Win ✅

C - Scissor
Scissor - Scissor = tie ✅
Scissor - Rock = Rock Win ✅
Scissor - Paper = Scissor Win ✅

"""

import random
item_list = ["Rock","Paper","Scissor"]

user_choice = input("Enter your move = Rock, Paper, Scissor = ")
comp_choice = random.choice(item_list)

print(f"User choice = {user_choice}, Computer choice = {comp_choice}")

if user_choice == comp_choice:
    print("Both Choices same : = Match Tie")

elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper Covers Rock = Computer Win")
    else:
        print("Rock Smashes Scissor = You Win")

elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor Cuts Paper = Computer Win")
    else:
        print("Paper covers Rock = You Win")

elif user_choice == "Scissor":
    if comp_choice == "Paper":
        print("Scissor Cuts Paper = You Win")
    else:
        print("Paper covers Rock = You Win")
R