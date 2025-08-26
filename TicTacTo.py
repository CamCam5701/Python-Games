square1 = 0
square2 = 0
square3 = 0
square4 = 0
square5 = 0
square6 = 0
square7 = 0
square8 = 0
square9 = 0

player1Turn = True
Player2Turn = False

rounds = 0

board = [
    [square1, square2, square3],
    [square4, square5, square6],
    [square7, square8, square9]
]

def print_board():
    print("- 1 2 3")
    for idx, row in enumerate(board, start=1):
        print(f"{idx} " + " ".join(str(cell) for cell in row))

print_board()

game_active = True

# while game_active:
if player1Turn:
    player1input = input("It is player 1's turn, please enter space 1-9: ")

    print(player1input)

    if player1input == "1":
        if square1 == 0:
            square1 = "O"
            board[0][0] = "O"
            player1Turn = False
            Player2Turn = True
            rounds += 1
            print_board()
    elif player1input == "2":
        if square2 == 0:
            square2 = "O"
            board[0][1] = "O"
            player1Turn = False
            Player2Turn = True
            rounds += 1
            print_board()
    elif player1input == "3":
        if square3 == 0:
            square3 = "O"
            board[0][2] = "O"
            player1Turn = False
            Player2Turn = True
            rounds += 1
            print_board()
    elif player1input == "4":
        if square4 == 0:
            square4 = "O"
            board[1][0] = "O"
            player1Turn = False
            Player2Turn = True
            rounds += 1
            print_board()
    elif player1input == "5":
        if square5 == 0:
            square5 = "O"
            board[1][1] = "O"
            player1Turn = False
            Player2Turn = True
            rounds += 1
            print_board()
    elif player1input == "6":
        if square6 == 0:
            square6 = "O"
            board[1][2] = "O"
            player1Turn = False
            Player2Turn = True
            rounds += 1
            print_board()
    elif player1input == "7":
        if square7 == 0:
            square7 = "O"
            board[2][0] = "O"
            player1Turn = False
            Player2Turn = True
            rounds += 1
            print_board()
    elif player1input == "8":
        if square8 == 0:
            square8 = "O"
            board[2][1] = "O"
            player1Turn = False
            Player2Turn = True
            rounds += 1
            print_board()
    elif player1input == "9":
        if square9 == 0:
            square9 = "O"
            board[2][2] = "O"
            player1Turn = False
            Player2Turn = True
            rounds += 1
            print_board()
    else:
        print("ERROR - invalid input, please try again")
    