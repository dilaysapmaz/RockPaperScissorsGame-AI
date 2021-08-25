from random import randint
# Nur İmece,Dilay Sapmaz
# 20.11.2019
'''
Player 3:
Rule is: the computer does his moves same with the player. 
First it is random. Then, if player r, computer's next move will be rock 
'''

# we create the array which contain Rock = "r", Paper="p", Scissors="s"
t = ["r", "p", "s"]

# we assign the array of element random "r", "s", "p"
computer = t[randint(0,2)]

# we create temp boolean to continue
temp = False

while temp == False:
# we take the input from user
    player = input("Rock (r), Paper (p), Scissors (s)?")
# if input value and computer value equals next time computer choose the the same one.
    if player == computer:
        print("Draw!")
        computer = player
        print(computer)
# Computer always choose the user value doesn't mather win or lose
    elif player == "r":
        if computer == "p":
            print("You lose!", computer, "covers", player)
           # computer = 'r'
            computer=player
            print(computer)
        else:
            print("You win!", player, "smashes", computer)
            #computer = 'r'
            computer=player
            print(computer)
    elif player == "p":
        if computer == "s":
            print("You lose!", computer, "cut", player)
            #computer = 'p'
            computer=player
            print(computer)
        else:
            print("You win!", player, "covers", computer)
            #computer = 'p'
            computer=player
            print(computer)
    elif player == "s":
        if computer == "r":
            print("You lose...", computer, "smashes", player)
            #computer = 's'
            computer=player
            print(computer)
        else:
            print("You win!", player, "cut", computer)
            #computer = 's'
            computer=player
            print(computer)
    else:
        print("That's not a valid play. Check your spelling!")

    # it necessary to continue game
    temp = False
