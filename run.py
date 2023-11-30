from random import randint

scores = {'computer': 0, 'player': 0}


class Hive:
    """
    The game is played on a board representing a hive. This class sets the
    board size, the number of bees, the player's names and the hive type
    """

    def __init__(self, size, num_bees, name, type):
        self.size = size
        self.hive = [["." for x in range(size)] for y in range(size)]
        self.num_bees = num_bees
        self.name = name
        self.type = type
        self.guesses = []
        self.bees = []

    def guess(self, x, y):
        """
        Adds previously guessed co-ordinates to guesses list
        """
        self.guesses.append((x, y))
        self.hive[x][y] = 'x'


    def add_bee():
        print('add_bee')


def random_point():
    """
    Helper function to return random integer that fits in the hive
    """
    print('random_point')


def validate_guess():
    print('validate_guess')


def place_bees():
    print('place_bees')


def play_game():
    print('play_game')


def new_game():
    """
    Starts new game. Sets the bees in the hives with correct number
    of bees, resets the scores and initialises the hives
    """

    size = 10
    num_bees = 6
    scores['computer'] = 0
    scores['player'] = 0
    print('Welcome to Free the Bees!')
    print("In a dystopian time, bees are hungry and can't escape their hive")
    print('You have stumbled across a beehive and want to help')
    print('Try to give the bees nectar without destroying their home')
    print(f'The hive is {size} squares long and high')
    print(f'There are {num_bees} bees to find in each hive')
    print('Feed all the bees before the computer to win!')
    print('Feed the bees by guessing a coordinate eg A0')
    print('Use letters for the x-axis (horizontal) and numbers for the y-axis (vertical)')
    name = input('Please give your name so the bees can say thanks!\n')


random_point()


validate_guess()


place_bees()


play_game()


new_game()