import random
user_win=0
computer_win=0
choice=["Rock","Paper","Scissor"]
print("Let's start our game 🎮🎮")

playing = input("Do you want to play this game? Yes/No: ")
if playing.lower() == "no":
    print("Exiting the game")
    quit()
else:
    print("Welcome to the game!!")

