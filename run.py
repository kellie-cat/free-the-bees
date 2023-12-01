from random import randint

scores = {'computer': 0, 'player': 0}

class Hive:
    """
    The game is played on a board representing a hive. This class sets the
    board size, the number of bees, the player's names and the hive type
    """

    def __init__(self, size, num_bees, name, hive):
        self.size = size
        self.hive = hive
        self.num_bees = num_bees
        self.name = name
        self.guesses = []
        self.bees = []

    def make_letters_to_numbers():
        letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
        return letters_to_numbers

    def print_hive(self):
        print("  A B C D E F G H")
        print("  +-+-+-+-+-+-+-+")
        row_number = 1
        for row in self.hive:
            print("%d|%s|" % (row_number, "|".join(row)))
            row_number += 1

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

    def add_bee(self, x, y, hive='computer'):
        print('add_bee')


def random_point(size):
    """
    Helper function to return random integer that fits in the hive
    """
    return randint(0, size-1)


def validate_guess():
    print('validate_guess')


def place_bees(hive):
    return place_bees


def play_game():
    print('play_game')


def new_game():
    """
    Starts new game. Sets the bees in the hives with correct number
    of bees, resets the scores and initialises the hives
    """
    size = 8
    num_bees = 5
    computer_hive = Hive(size, num_bees, 'Computer', hive='computer')
    player_hive = Hive(size, num_bees, 'Player', hive='player')

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
    print('Use letters for x-axis (horizontal), numbers for y-axis (vertical)')
    name = input('Please give your name so the bees can say thanks!\n')

    for _ in range(num_bees):
        place_bees(computer_hive)
        place_bees(player_hive)

    Hive.print_hive(player_hive)


play_game()


new_game()
