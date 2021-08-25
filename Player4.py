from random import randint

#this array, computer's array
t = ["r", "p", "s"]

#we are throwing a random number here. It should be 0,1 or 2. 0 means rock, 1 means paper and 2 means scissors.
computer = t[randint(0,2)]

#the values that we will be using. Assignin all to the zero for blocking any errors.
counterR=0
counterS=0
counterP=0
i=0
#we created a temp boolean value. we assignted it to false because this is going to be our control
#value for while loop.temp = False
temp = False
# This list is for our statistical rule-based system. We created it with size 7 but it checks for 6.
#It is going to be play with looking the player's last 6 moves.
list = ['r','s','p','r','s','p','r']
while temp == False:

    player = input("Rock (r), Paper (p), Scissors (s)?")#Player1 task. Asking r p or s
    #and all other things are checking for who is going to be winner and print functions.

    # inserting array's first place if player's moves are r p and s
    if( player == "r" or player== "p" or player=="s"):
        list.insert(0,player)
        print(list)

    counterR=0
    counterS=0
    counterP=0

    #increasing counters based on the list array's elements
    for x in range(6):
        if(list[x]== "r"):
            counterR=counterR+1
        elif(list[x]== "p"):
            counterP=counterP+1
        elif(list[x]=="s"):
            counterS=counterS+1
        print("R",counterR,"P",counterP,"S",counterS)

    #making the computer's decisions based on what is greater than others. These are player's moves.
    if (counterR>counterP) and ( counterR > counterS ):
        computer= "p"
    elif (counterP>counterR) and ( counterP> counterS ):
        computer= "s"
    elif (counterS>counterP) and ( counterS > counterR ):
        computer= "r"
    else:
        computer = t[randint(0,2)] #if they are equal, throw it random

    #and all other things are checking for who is going to be winner and print functions.
    if player == computer:
        print("Draw!")
        print(computer)
    elif player == "r":
        if computer == "p":
            print("You lose!", computer, "covers", player)
            print("computer",computer)
        else:
            print("You win!", player, "smashes", computer)
            print("computer",computer)
    elif player == "p":
        if computer == "s":
            print("You lose!", computer, "cut", player)
            print("computer",computer)
        else:
            print("You win!", player, "covers", computer)
            print("computer",computer)
    elif player == "s":
        if computer == "r":
            print("You lose...", computer, "smashes", player)
            print("computer",computer)
        else:
            print("You win!", player, "cut", computer)
            print("computer",computer)
    else:
        print("That's not a valid play. Check your spelling!")
    #temp was set to True, but we want it to be False so the loop continues


    temp = False
    #we deleted the random variable command because we dont want the dumb computer.




