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


def start_game():
    print('Welcome to Free the Bees!')
    name = input('Please tell us your name so the bees can say thanks!\n')
    if name == '' or '0':
        print("Please give a name - bees don't like strangers!")
        name = input('Please tell us your name so the bees can say thanks!\n')

start_game()