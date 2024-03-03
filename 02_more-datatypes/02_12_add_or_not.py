# MEMORY GAME WITH SETS
# Continuously collect number input from a user with a `while` loop.
# Confirm that the input can be converted to an integer,
# then add it to a Python `set()`.
# If the element was already in the set, notify the user that their
# their input is a duplicate and deduct a point.
# If the user loses 5 points, quit the program.
# They win if they manage to create a set that has more than 10 items.

import os
from getpass import getpass

final_set = set()
fail_counter = 0
uin = ""

os.system('clear')
print(f"Welcome to the memory game, Goal create a list of 11 unique numbers. If you fail 5 times you will loose the game.")


while uin != 'e':
    uin = getpass("Please enter a number that you have not entered before.. or type \"e\" to exit: ")
    print("\n\n")
    if uin.isalpha():
        uin = uin.lower()
        if uin == 'e':
            print("Thanks for playing")
            exit()
        else:
            print("You did not enter a number.. ")
            continue
    if uin.isnumeric():
        uin = int(uin)
        if uin not in final_set:
            final_set.add(uin)
            print("Good one...\n\n")
        else:
            fail_counter += 1
            print(f"You have already entered that number: you can only make that mistake {5 - fail_counter} more times.")

    if fail_counter >= 5:
        print("You have lost the game")
        exit()
    elif len(final_set) > 10:
        print("Congrats you have won the game and created a list of 10 numbers")
        print(final_set)
        exit()
        
