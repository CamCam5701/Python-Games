money = 100.00
mainMenu = True
game = False
bet = 0
betProcess = False
gambleSetup = False
count = 0

seed = int(money * 917254)

gamblingCode = True
while gamblingCode:

    def rand1or2(bet, global_count):
        global seed
        mix = int(bet * 179854) + (global_count & 0x7fffffff)
        seed = (seed + mix) & 0x7fffffff
        seed = (seed * 1103515245 + 12345) % 2147483648
        return 1 + (seed % 2)

    while mainMenu:
        print("""Welcome to Cams Casino, please select a game:
Press 1 for Mines
Press 2 for Coin Toss
Press 0 to Exit
You have $""" + str(money) + """

Version 1.0""")
        gameSelction = input()
        if gameSelction == "1":
            game = True
            mainMenu = False
        elif gameSelction == "2":
            game = True
            mainMenu = False
        elif gameSelction == "0":
            print("Thank you for visiting Cams Casino, goodbye!")
            game = False
            mainMenu = False
            gamblingCode = False
        else:
            print("""-------------
INVALID INPUT
-------------""")

    while game:
        if gameSelction == "1":
            print("Mines is currently in development, please select another game")
            game = False
            mainMenu = True
        elif gameSelction == "2":
            betProcess = True
            while betProcess:
                print("How much would you like to bet? Minimum bet is $0.01, maximum bet is $" + str(money))
                bet = float(input())
                if bet > money:
                    print("""
---ERROR---
You cannot bet more money than you have!
Please try again!
""")
                elif bet < 0.01:
                    print("""
---ERROR---
You must bet at least $0.01!
Please try again!
""")
                else:
                    betProcess = False
                    gambleSetup = True
            while gambleSetup:
                print("You have bet $" + str(bet) + ", please select Heads or Tails")
                print("Press 1 for Heads or 3 for Tails")
                coinInput = input()
                if coinInput == "1":
                    coinInput = "Heads"
                    gambleSetup = False
                elif coinInput == "3":
                    coinInput = "Tails"
                    gambleSetup = False
                else:
                    print("""
---ERROR---
Invalid Input
Please try again!
""")
            # call RNG once, use the result and advance the round counter
            flip = rand1or2(bet, count)
            count += 1
            if flip == 1:
                coinResult = "Heads"
            else:
                coinResult = "Tails"
            if coinInput == coinResult:
                print("The coin landed on " + coinResult + ", you win!")
                money = money + bet
                print("You now have $" + str(money))
                print("Press Enter to continue...")
                input()
                game = False
                mainMenu = True
                bet = 0
            else:
                print("The coin landed on " + coinResult + ", you lose!")
                money = money - bet
                if money < 0.01:
                    print("You now have $" + str(money) + ", you are out of money!")
                    print("Game Over! Press Enter to exit")
                    input()
                    game = False
                    mainMenu = False
                    bet = 0
                else:
                    print("You now have $" + str(money))
                    print("Press Enter to continue")
                    input()
                    game = False
                    mainMenu = True
                    bet = 0
