player1 = 'O'
player2 = 'X'

one_one = 0
one_two = 0
one_three = 0
two_one = 0
two_two = 0
two_three = 0
three_one = 0
three_two = 0
three_three = 0

player1Turn = True
Player2Turn = False

rounds = 0

board = [
    [one_one, one_two, one_three],
    [two_one, two_two, two_three],
    [three_one, three_two, three_three]
]

def print_board():
    print("- 1 2 3")
    for idx, row in enumerate(board, start=1):
        print(f"{idx} " + " ".join(str(cell) for cell in row))

print_board()

game_active = True

#while game_active:
if player1Turn:
    player1input1 = input("It is player 1's turn, please enter the column number of an avalible space: ")
    player1input2 = input("please enter the row number of an avalible space: ")
    player1inputs = int(player1input1), int(player1input2)
    if player1inputs == (1, 1):
        if one_one == 0:
            one_one = player1
            player1Turn = False
            Player2Turn = True
            rounds += 1
            print_board()
    elif player1inputs == (1, 2):
        if one_two == 0:
            one_two = player1
            player1Turn = False
            Player2Turn = True
            rounds += 1
            print_board()
    elif player1inputs == (1, 3):
        if one_three == 0:
            one_three = player1
            player1Turn = False
            Player2Turn = True
            rounds += 1
            print_board()
    elif player1inputs == (2, 1):
        if two_one == 0:
            two_one = player1
            player1Turn = False
            Player2Turn = True
            rounds += 1
            print_board()