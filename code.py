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

while True:
    user_input=input("Type Rock/Paper/Scissor or Q to exit")
    if user_input.lower()=='Q':
        print("Quiting the game.")
        break
    if user_input not in choice:
        print("There is no such options.")
        continue
    

   

