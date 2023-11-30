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
    print('new_game')


random_point()


validate_guess()


place_bees()


play_game()


new_game()