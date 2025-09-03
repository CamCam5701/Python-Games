mainMenuLoop = True
game = False

while mainMenuLoop:
    def mainMenu():
        print("""Welcome to Cams Casino, please select a game:
Press 1 for Mines
Press 2 for Coin Toss

Version 0.0""")
        gameSelction = input()
        if gameSelction == "1":
            game = True
            mainMenuLoop = False
        elif gameSelction == "2":
            game = True
            mainMenuLoop = False
        else:
            print("INVALID INPUT")

mainMenu()
