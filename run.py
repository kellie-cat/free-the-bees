from random import randint

scores = {'computer': 0, 'player': 0}


class Hive:
    """
    The game is played on a board representing a hive. This class sets the
    board size, the number of bees, the player's names and the hive type
    """

    def __init__(self, size, num_bees, name, type):
        self.size = size
        self.hive = [["|" for x in range(size)] for y in range(size)]
        self.num_bees = num_bees
        self.name = name
        self.type = type
        self.guesses = []
        self.bees = []

    def print_hive(hive):
        for row in self.hive:
            print("|".join(row))

    def guess(self, x, y):
        """
        Adds previously guessed co-ordinates to guesses list
        """
        self.guesses.append((x, y))
        self.hive[x][y] = 'x'

        if (x, y) in self.bees:
            self.hive[x][y] = '*'
            return 'Dinnertime for the bees!'
        else:
            return 'Still hungry :('

    def add_bee(self, x, y, type='computer'):
        print('add_bee')


def random_point(size):
    """
    Helper function to return random integer that fits in the hive
    """
    return randint(0, size-1)


def validate_guess():
    print('validate_guess')


def place_bees(hive):
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

    computer_hive = Hive(size, num_bees, 'Computer', type='computer')
    player_hive = Hive(size, num_bees, name, type='player')

    for _ in range(num_bees):
        place_bees(computer_hive)
        place_bees(player_hive)


play_game()


new_game()
