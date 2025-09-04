money = 100.00
mainMenu = True
game = False

while mainMenu:
    print("""Welcome to Cams Casino, please select a game:
Press 1 for Mines
Press 2 for Coin Toss

Version 0.0""")
    gameSelction = input()
    if gameSelction == "1":
        game = True
        mainMenu = False
    elif gameSelction == "2":
        game = True
        mainMenu = False
    else:
        print("INVALID INPUT")

while game:
    print("You have $" + str(money))