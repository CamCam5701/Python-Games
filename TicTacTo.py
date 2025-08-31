square1 = "#"
square2 = "#"
square3 = "#"
square4 = "#"
square5 = "#"
square6 = "#"
square7 = "#"
square8 = "#"
square9 = "#"

game_active = False

player1Turn = True
player2Turn = False

rounds = 0

board = [
    [square1, square2, square3],
    [square4, square5, square6],
    [square7, square8, square9]
]

def print_board():
    for row in board:
        print(" ".join(str(cell) for cell in row))

mainMenu = """
Welcome to Tic Tac Toe
Press 1 to start the game
Press 2 to veiw the tutorial
Press 3 to veiw links to the
github repo
Press 4 to exit
"""

menuActive = True

while menuActive:
    print(mainMenu)
    menuInput = input()

    if menuInput == "1":
        game_active = True
        menuActive = False
        print_board()
    elif menuInput == "2":
        print("""
Player 1 is O and player 2 is X
First player to get 3 in a row
wins
To place your piece, enter a
number 1-9 that corresponds to
the board space for example: 1
would be the bottom left space
and 9 would be the top right
space etc.
Press enter to return to the""")
        input("main menu")
    elif menuInput == "3":
        linkInput = input("type 1 for full link link, type 2 for shorten link, or type 3 to return to the main menu: ")
        if linkInput == "1":
            print("https://github.com/CamCam5701/Tic-Tac-Toe")
            input("""Press enter to return to the
main menu""")
        elif linkInput == "2":
            print("https://rb.gy/0euqt4")
            input("""Press enter to return to the
main menu""")
        elif linkInput == "3":
            print("")
    elif menuInput == "4":
        menuActive = False


while game_active:
    if rounds == 9:
        input("The game has ended! Press enter to exit")
        plauer1Turn = False
        player2Turn = False
        game_active = False
    if player1Turn:
        print("It is player 1's turn, you are")
        print("O, please enter space 1-9: ")
        player1input = input()
        if player1input == "1":
            if square1 == "#":
                square1 = "O"
                board[2][0] = "O"
                rounds += 1
                print_board()
                player2Turn = True
                Player1Turn = False
        elif player1input == "2":
            if square2 == "#":
                square2 = "O"
                board[2][1] = "O"
                rounds += 1
                print_board()
                player2Turn = True
                Player1Turn = False
        elif player1input == "3":
            if square3 == "#":
                square3 = "O"
                board[2][2] = "O"
                rounds += 1
                print_board()
                player2Turn = True
                Player1Turn = False
        elif player1input == "4":
            if square4 == "#":
                square4 = "O"
                board[1][0] = "O"
                rounds += 1
                print_board()
                player2Turn = True
                Player1Turn = False
        elif player1input == "5":
            if square5 == "#":
                square5 = "O"
                board[1][1] = "O"
                rounds += 1
                print_board()
                player2Turn = True
                Player1Turn = False
        elif player1input == "6":
            if square6 == "#":
                square6 = "O"
                board[1][2] = "O"
                rounds += 1
                print_board()
                player2Turn = True
                Player1Turn = False
        elif player1input == "7":
            if square7 == "#":
                square7 = "O"
                board[0][0] = "O"
                rounds += 1
                print_board()
                player2Turn = True
                Player1Turn = False
        elif player1input == "8":
            if square8 == "#":
                square8 = "O"
                board[0][1] = "O"
                rounds += 1
                print_board()
                player2Turn = True
                Player1Turn = False
        elif player1input == "9":
            if square9 == "#":
                square9 = "O"
                board[0][2] = "O"
                rounds += 1
                print_board()
                player2Turn = True
                Player1Turn = False

    #---------------END OF PLAYER 1 TURN---------------

    if rounds == 9:
        input("The game has ended! Press enter to exit")
        plauer1Turn = False
        player2Turn = False
        game_active = False

    if player2Turn:
        print("It is player 2's turn, you are")
        print("X, please enter space 1-9: ")
        player2input = input()
        if player2input == "1":
            if square1 == "#":
                square1 = "X"
                board[2][0] = "X"
                rounds += 1
                print_board()
                player1Turn = True
                player2Turn = False
        elif player2input == "2":
            if square2 == "#":
                square2 = "X"
                board[2][1] = "X"
                rounds += 1
                print_board()
                player1Turn = True
                player2Turn = False
        elif player2input == "3":
            if square3 == "#":
                square3 = "X"
                board[2][2] = "X"
                rounds += 1
                print_board()
                player1Turn = True
                player2Turn = False
        elif player2input == "4":
            if square4 == "#":
                square4 = "X"
                board[1][0] = "X"
                rounds += 1
                print_board()
                player1Turn = True
                player2Turn = False
        elif player2input == "5":
            if square5 == "#":
                square5 = "X"
                board[1][1] = "X"
                rounds += 1
                print_board()
                player1Turn = True
                player2Turn = False
        elif player2input == "6":
            if square6 == "#":
                square6 = "X"
                board[1][2] = "X"
                rounds += 1
                print_board()
                player1Turn = True
                player2Turn = False
        elif player2input == "7":
            if square7 == "#":
                square7 = "X"
                board[0][0] = "X"
                rounds += 1
                print_board()
                player1Turn = True
                player2Turn = False
        elif player2input == "8":
            if square8 == "#":
                square8 = "X"
                board[0][1] = "X"
                rounds += 1
                print_board()
                player1Turn = True
                player2Turn = False
        elif player2input == "9":
            if square9 == "#":
                square9 = "X"
                board[0][2] = "X"
                rounds += 1
                print_board()
                player1Turn = True
                player2Turn = False
