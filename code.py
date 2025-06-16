import random
user_win=0
computer_win=0
draw=0
choice=["rock","paper","scissor"]
print("Let's start our game 🎮🎮")

playing = input("Do you want to play this game? Yes/No: ").lower() 
if playing== "no":
    print("Exiting the game")
    quit()
else:
    print("Welcome to the game!!")

while True:
    user_input=input("Type Rock/Paper/Scissor or Q to exit: ").lower()
    if user_input=='q':
        print("Quiting the game.")
        break


    if user_input not in choice:
        print("There is no such options.")
        continue

    random_number=random.randint(0,2)
    # 0=Rock, 1=Paper, 2=Scissor

    computer_input= choice[random_number]

    if(user_input=="rock" and computer_input=="scissor"):
        print("You win")
        user_win+=1
    elif (user_input=="rock" and computer_input=="paper"):
        print("You lost. Computer wins")
        computer_win+=1
    elif (user_input=="rock" and computer_input=="rock"):
        print("It's a draw")
        draw+=1

    elif(user_input=="paper" and computer_input=="rock"):
        print("You win")
        user_win+=1
    elif (user_input=="paper" and computer_input=="scissor"):
        print("You lost. Computer wins")
        computer_win+=1
    elif (user_input=="paper" and computer_input=="paper"):
        print("It's a draw")
        draw+=1

    elif(user_input=="scissor" and computer_input=="paper"):
        print("You win")
        user_win+=1
    elif (user_input=="scissor" and computer_input=="rock"):
        print("You lost. Computer wins")
        computer_win+=1
    elif (user_input=="scissor" and computer_input=="scissor"):
        print("It's a draw")
        draw+=1

print("\nGame Over! 🎮")
print("Final Score:")
print("You won:", user_win, "time(s)")
print("Computer won:", computer_win, "time(s)")
print("Draws:", draw)








   

