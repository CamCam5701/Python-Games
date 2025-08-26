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

board = [
    [one_one, one_two, one_three],
    [two_one, two_two, two_three],
    [three_one, three_two, three_three]
]

def print_board():
    for row in board:
        print(" ".join(str(cell) for cell in row))

print_board()