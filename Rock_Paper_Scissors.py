import random
import time

print("Let's play 'Rock, Papers, Scissors!'")

while True:
    print("Your turn! Please enter one of the following.\n Enter 1 for Rock.\n Enter 2 for Paper.\n Enter 3 for Scissor.\n")
    user_move = eval(input())
    user_move = "Rock" if user_move == 1 else "Paper" if user_move == 2 else "Scissor"
    print("You played ", user_move)
    time.sleep(1)
    computer_move = random.randint(1,3)
    computer_move = "Rock" if computer_move == 1 else "Paper" if computer_move == 2 else "Scissor"
    print("Computer played ", computer_move)
    time.sleep(1)
    if user_move == computer_move:
        print("Oops! It's a draw.\n")
    elif user_move == "Rock" and computer_move == "Paper" or user_move == "Paper" and computer_move == "Scissor" or user_move == "Scissor" and computer_move == "Rock":
        print("Unfortunately you lost!\n")
    else:
        print("Hurray! You won.\n")
    print("Wanna play more? Press Y/y to continue playing.\n")
    next_game = input()
    if next_game != 'Y' and next_game != 'y':
        break