from random import randint

#this array, computer's array
t = ["r", "p", "s"]

#we are throwing a random number here. It should be 0,1 or 2. 0 means rock, 1 means paper and 2 means scissors.
computer = t[randint(0,2)]

#we created a temp boolean value. we assignted it to false because this is going to be our control
#value for while loop.
temp = False

while temp == False:
    player = input("Rock (r), Paper (p), Scissors (s)?") #Player1 task. Asking r p or s
    #and all other things are checking for who is going to be winner and print functions.
    if player == computer:
        print("Draw!")
    elif player == "r":
        if computer == "p":
            print("You lose!", computer, "covers", player)
            print(computer)
        else:
            print("You win!", player, "smashes", computer)
            print(computer)
    elif player == "p":
        if computer == "s":
            print("You lose!", computer, "cut", player)
            print(computer)
        else:
            print("You win!", player, "covers", computer)
            print(computer)
    elif player == "s":
        if computer == "r":
            print("You lose...", computer, "smashes", player)
            print(computer)
        else:
            print("You win!", player, "cut", computer)
            print(computer)
    else: #the situation that the user enters something other than given things
        print("That's not a valid play. Check your spelling!")

    #temp was set to True, but we want it to be False so the loop continues
    temp = False
    computer = t[randint(0,2)] #This is the dumb one. So it throws random number for rock paper and scissors
                               #without any rule. It just throws.
