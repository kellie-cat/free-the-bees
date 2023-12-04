import unicodedata
from unicodedata import normalize

import random
from random import randint

import colorama
from colorama import Fore, Back, Style
colorama.init()

HIVE = [
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
]

NUM_BEES = 10
SIZE = 8


def start_game():
    print('Welcome to Free the Bees!')
    name = ''


while True:
    name = input("Please tell us your name so the bees can say thanks!\n")

    if len(name) < 2 or name.isnumeric() is True:
        print("That name is not valid, please enter a name with letters,\
              bees don't like strangers!")
        continue
    else:
        print(f'Thanks for helping the bees, {name}!')
        break

player_hive = HIVE


def make_random_coordinates(num_points, x_range, y_range):
    """
    Helper function to return random integer that fits in the hive
    """
    coordinates = []

    for _ in range(num_points):
        x = randint(x_range[0], x_range[1])
        y = randint(y_range[0], y_range[1])
        coordinates.append((x, y))

    print(coordinates)

random_coordinates = make_random_coordinates(10, (0, 7), (0, 7))

print(HIVE)
print("In a dystopian time, bees are hungry and can't escape their hive")
print('You have stumbled across a beehive and want to help')
print('Try to give the bees nectar without destroying their home')
print(f'The hive is {SIZE} squares long and high')
print(f'There are {NUM_BEES} bees to find in each hive')
print('Feed all the bees before the computer to win!')
print('Feed the bees by guessing a coordinate')
print('When prompted, input a number for x-axis (horizontal rows) first')
print('Then a number for the y-axis (vertical columns)')

def make_guess():
    row = input('Enter a number to guess the row the bee is on: \n')
    column = input('Enter a number to guess the column the bee is on: \n')


start_game()
