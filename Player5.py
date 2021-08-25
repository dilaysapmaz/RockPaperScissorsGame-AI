from random import randint
# Nur İmece,Dilay Sapmaz
# 20.11.2019
'''
Player 5:
Rule is: The computer first assigns a random value and the game starts.
If the user enters one of r s and t, it holds the values in an array. 
If the value is not entered, a warning message is displayed.
Counts and holds r, s, t.It calculates probability based on the values it finds.
according to this possibility the user finds the maximum option.
It makes  next choice based on this possibility.
'''

# we create the array which contain Rock = "r", Paper="p", Scissors="s"
t = ["r", "p", "s"]

# we assign the array of element random "r", "s", "p" and create counters for how many r,s,t contains in array
computer = t[randint(0, 2)]
counterR = 0
counterS = 0
counterP = 0
x = 0
# we create temp boolean to continue
temp = False
list = []
# create the array for hold the user value
while temp == False:
    # we take the input from user
    player = input("Rock (r), Paper (p), Scissors (s)?")

# every step, we hold the new user value in the first index
    if (player == "r" or player == "p" or player == "s"):
        list.insert(0, player)
        print(list)
# counting r,s,t
    if (list[x] == "r"):
        counterR = counterR + 1
    elif (list[x] == "p"):
        counterP = counterP + 1
    elif (list[x] == "s"):
        counterS = counterS + 1
    print("R", counterR, "P", counterP, "S", counterS)
# sum is the how many numbers the user entered
    sum = counterP + counterR + counterS
# We have found the probability that r, s or t and then multiple 1000 so as not to float
    probR = (counterR / sum) * 1000
    probS = (counterS / sum) * 1000
    probP = (counterP / sum) * 1000
# assign the random value range 0-1000
    random = randint(0, 1000)

# we define the range and then assign the value according to random value
    paperAralik = 0 + probR
    scissorsAralik = probR + probP
    rockAralik = probR + probP + probS
#we've assigned the value to beat it
    if (0 <= random and random <= paperAralik):
        computer = 'p'
    elif (paperAralik < random and random <= scissorsAralik):
        computer = 's'
    elif (scissorsAralik < random and random <= rockAralik):
        computer = 'r'

# According to the value entered by the user, we have shown on the screen that he lose or win.
    if player == computer:
        print("Draw!")
        print(computer)
    elif player == "r":
        if computer == "p":
            print("You lose!", computer, "covers", player)
            print("computer", computer)
        else:
            print("You win!", player, "smashes", computer)
            print("computer", computer)
    elif player == "p":
        if computer == "s":
            print("You lose!", computer, "cut", player)
            print("computer", computer)
        else:
            print("You win!", player, "covers", computer)
            print("computer", computer)
    elif player == "s":
        if computer == "r":
            print("You lose...", computer, "smashes", player)
            print("computer", computer)
        else:
            print("You win!", player, "cut", computer)
            print("computer", computer)
    else:
        print("That's not a valid play. Check your spelling!")

    # for the loop continues
    temp = False




