import random

player = input("Enter ypur Name :")


playerscore = 0
computerscore = 0

def playerbat():
    while True:
        run = int(input("Enter your run : "))
        if run > 6:
            print("Error move")
            continue
        compbowl = random.randint(1,2)
        print("Computer bowled : ",compbowl)
        if run == compbowl:
            break
        else:
            playerscore = playerscore + run

def playerbowl():
    while True:
        run = int(input("Enter your bowl"))
        if run > 6:
            print("Error move")
            continue
        compbat = random.randint(1,2)
        print("Computer batted : ",compbat)
        if run == compbat:
            break
        else:
            computerscore = computerscore + compbat

replay = 1
while (replay != 0):
    
    choice = int(input("Enter 1 to bat first or Enter 2 to ball first"))
    if(choice == 1):
        playerbat()
        print("Player got out")
        playerbowl()
    elif (choice == 2):
        playerbowl()
        print("Computer got out")
        playerbat()

    if playerscore > computerscore:
        print(player,"wins")
    elif playerscore < computerscore:
        print("Computer wins")
    else:
        print("Its a draw")

    replay = int(input("Enter 0 to exit else enter any number to continue"))
    if replay != 0:
        print("!!!Next Game Begins!!!")
        playerscore = 0
        computerscore = 0