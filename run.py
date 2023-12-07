import unicodedata
from unicodedata import normalize

import os

import random
from random import randint

import colorama
from colorama import Fore, Back, Style
colorama.init()

NUM_BEES = 10
SIZE = 8
HIVE = []
# Hive for player to make guesses to locate bees on, no bees visible until fed
PLAYER_HIVE = [[' '] * SIZE for x in range(SIZE)]
# Hive for player to place bees and computer to make guesses on
COMPUTER_HIVE = [[' '] * SIZE for x in range(SIZE)]


def cls():
    os.system('cls')


# now, to clear the screen
cls()


def print_hive(HIVE):
    """
    Make HIVE
    """
    for i in range(0, SIZE):
        HIVE.append(['0'] * SIZE)

    """
    Tidies up the hive
    """
    for row in HIVE:
        print((" ").join(row))


def print_intro():
    print("In a dystopian time, bees are hungry and can't escape their hive")
    print('You have stumbled across a beehive and want to help')
    print('Try to give the bees nectar without destroying their home')
    print(f'The hive is {SIZE} squares long and high')
    print(f'There are {NUM_BEES} bees to find in each hive')
    print('Feed all the bees before the computer to win!')
    print('Feed the bees by guessing a coordinate')
    print('When prompted, input a number for x-axis (horizontal rows) first')
    print('Then a number for the y-axis (vertical columns)')


def get_player_name():
    while True:
        player = input("Please tell us your name so the bees can say "
                       "thanks!\n")
        if len(player) >= 2 and not player.isnumeric():
            print(f'Thanks for helping the bees, {player}!')
            break
        else:
            print("That name is not valid, please enter a name with letters,"
                  " bees don't like strangers!")


"""
def make_random_coordinates(num_points, x_range, y_range):

    Helper function to return random integer that fits in the hive

    coordinates = []

    for _ in range(num_points):
        x = randint(x_range[0], x_range[1])
        y = randint(y_range[0], y_range[1])
        coordinates.append((x, y))

    coordinates = 'X'
"""
"""
random_coordinates = make_random_coordinates(10, (0, 7), (0, 7))
"""


def create_bees(HIVE):
    for bee in range(SIZE):
        bee_row, bee_column = randint(0, 7), randint(0, 7)
        while HIVE[bee_row][bee_column] == "X":
            bee_row, bee_column = make_guess()
        HIVE[bee_row][bee_column] = "X"


def make_guess():
    turn = 0
    if turn in range(5):
        while True:
            row = input("Enter a number between 0 - 7 to guess the ROW of "
                        "the bee: \n")
            if row.isdigit() and 0 <= int(row) <= 7:
                break
            elif not row.isdigit():
                print("A letter or space is not an appropriate choice, please"
                      " enter a number")
            elif int(row) >= 8:
                print("That choice is too big. Pick a number between 0 - 7")
            else:
                print("That's not an appropriate choice, please select a "
                      "valid row by picking a number from 0 - 7, then return")

        while True:
            column = input("Enter a number between 0 - 7 to guess the "
                           "COLUMN of the bee: \n")
            if column.isdigit() and 0 <= int(column) <= 7:
                break
            elif not column.isdigit():
                print("A letter or space is not an appropriate choice, please"
                      " enter a number")
            elif int(column) >= 8:
                print("That choice is too big. Pick a number between 0 - 7")
            else:
                print("That's not an appropriate choice, please select a "
                      "valid column by picking a number from 0 - 7, then "
                      "return")

        return int(row), int(column)
        turn += 1


def count_fed_bees(hive):
    count = 0
    for row in hive:
        for column in row:
            if column == 'X':
                count += 1
    return count


def start_game():
    create_bees(PLAYER_HIVE)
    create_bees(COMPUTER_HIVE)

    turn = 5
    while turn > 0:
        print('Guess a bee location')
        print_hive(COMPUTER_HIVE)
        row, column = make_guess()
        if PLAYER_HIVE[row][column] == "-":
            print("You guessed that one already.")
            turn -= 1
        elif COMPUTER_HIVE[row][column] == "X":
            print(Fore.GREEN + "Well done, you FED a bee!" + Fore.RESET)
            PLAYER_HIVE[row][column] = "X"
        else:
            print(Fore.RED + "Sorry, you MISSED!" + Fore.RESET)
            PLAYER_HIVE[row][column] = "-"
            turn -= 1
        if count_fed_bees(PLAYER_HIVE) == NUM_BEES:
            print("You win!")
            break
        print("You have" + str(turn) + "turns left")
        if turn == 0:
            print("You ran out of turns")
            break


if __name__ == "__main__":
    print_intro()
    get_player_name()
    start_game()
