SIZE = 8
player_bee_coordinates = [(0, 4), (3, 3)]


def welcome_screen():
    """
    Print Welcome Message in Title Art font and press enter to continue
    """
    print('Welcome to FREE THE BEES')


welcome_screen()


def display_hive():
    """
    Display player hive (with hidden bees and guesses) and computer hive
    (visible bees and computer guesses)
    """
    print('Display player hive')
    print('Display computer hive')


def display_instructions():
    """
    Show instructions
    """
    print('Instructions')


def place_bees():
    """
    In computer hive, asks for bee_row, bee_column input, stores them in
    computer_bee_coordinates
    In player hive, creates and returns random player_bee_coordinates
    """
    bee_row = input('Please input a row you would like to place a bee:')
    bee_column = input('Please input a column you would like to place a bee:')
    computer_bee_coordinates = bee_row, bee_column
    return computer_bee_coordinates


def player_won_results():
    print('Well done for feeding all the bees! You saved the hive!')
    input(f'If you would like to play again to save another hive, press'
          ' "P", if you would like to exit the game, press "E":')


def player_guess():
    player_guess_list = []
    player_bee_coordinates = []
    guess = 0
    fed = 0
    for guess in range(0, 2):
        guess_row = input('Please guess a row you think a bee is on:')
        guess_column = input('Please guess a column you think a bee is on:')
        player_guess_coordinates = (guess_row, guess_column)
        print('Add player_guess_coordinates to player_guess_list')
        if player_guess_coordinates in player_guess_list:
            print('You already tried that area, no bees! Try again!')
        if player_guess_coordinates in player_bee_coordinates:
            print('You found a bee!')
            fed += 1
        else:
            print('No bee there, keep trying!')
    player_guess_list.append(player_guess_coordinates)
    guess += 1
    if fed == 10:
        print('Congratulations! You fed all the bees!')
        player_won_results()


def computer_guess():
    print('Random computer guess')
    check_computer_answer()


def check_computer_answer():
    print('Check if the computer fed a bee')


def start_game():
    player = input('What is your name?')
    print(f'Welcome, {player}')
    display_hive()

    display_instructions()

    place_bees()

    player_guess()

    computer_guess()


start_game()
