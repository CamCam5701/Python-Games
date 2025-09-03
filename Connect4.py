player1 = "O"
player2 = "X"

# start of board variables

one_one = 0
one_two = 0
one_three = 0
one_four = 0
one_five = 0
one_six = 0
one_seven = 0
one_eight = 0
one_nine = 0
two_one = 0
two_two = 0
two_three = 0
two_four = 0
two_five = 0
two_six = 0
two_seven = 0
two_eight = 0
two_nine = 0
three_one = 0
three_two = 0
three_three = 0
three_four = 0
three_five = 0
three_six = 0
three_seven = 0
three_eight = 0
three_nine = 0
four_one = 0
four_two = 0
four_three = 0
four_four = 0
four_five = 0
four_six = 0
four_seven = 0
four_eight = 0
four_nine = 0
five_one = 0
five_two = 0
five_three = 0
five_four = 0
five_five = 0
five_six = 0
five_seven = 0
five_eight = 0
five_nine = 0
six_one = 0
six_two = 0
six_three = 0
six_four = 0
six_five = 0
six_six = 0
six_seven = 0
six_eight = 0
six_nine = 0
seven_one = 0
seven_two = 0
seven_three = 0
seven_four = 0
seven_five = 0
seven_six = 0
seven_seven = 0
seven_eight = 0
seven_nine = 0
eight_one = 0
eight_two = 0
eight_three = 0
eight_four = 0
eight_five = 0
eight_six = 0
eight_seven = 0
eight_eight = 0
eight_nine = 0
nine_one = 0
nine_two = 0
nine_three = 0
nine_four = 0
nine_five = 0
nine_six = 0
nine_seven = 0
nine_eight = 0
nine_nine = 0

# end of board variables

grid = [
    [one_one, one_two, one_three, one_four, one_five, one_six, one_seven, one_eight, one_nine],
    [two_one, two_two, two_three, two_four, two_five, two_six, two_seven, two_eight, two_nine],
    [three_one, three_two, three_three, three_four, three_five, three_six, three_seven, three_eight, three_nine],
    [four_one, four_two, four_three, four_four, four_five, four_six, four_seven, four_eight, four_nine],
    [five_one, five_two, five_three, five_four, five_five, five_six, five_seven, five_eight, five_nine],
    [six_one, six_two, six_three, six_four, six_five, six_six, six_seven, six_eight, six_nine],
    [seven_one, seven_two, seven_three, seven_four, seven_five, seven_six, seven_seven, seven_eight, seven_nine],
    [eight_one, eight_two, eight_three, eight_four, eight_five, eight_six, eight_seven, eight_eight, eight_nine],
    [nine_one, nine_two, nine_three, nine_four, nine_five, nine_six, nine_seven, nine_eight, nine_nine]
]

print("1 2 3 4 5 6 7 8 9")

for row in grid:
    print(" ".join(str(cell) for cell in row))

player1_turn = True
player2_turn = False

input("Press Enter to end")