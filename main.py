from ascii import title, thank_you, have_fun
from gridhelp import grid_coor, grid_ex

# +------------------------------ INTRODUCTION -----------------------------------+
print(title)
print('Welcome to a game of Tic Tac Toe!')
print('Two players "O" and "X" will compete against each other where the first to make a line across the board, '
      'may it be horizontal, vertical, or slanted, wins!')
print(f'\nThe grid of the board is set up like so:\n{grid_coor}')
print(f'\nTo place your move, simply type in a number based on the grid system.\nFor example, typing 1 would result '
      f'to:\n{grid_ex}\n')
print(have_fun)

# +------------------------------ GAME -----------------------------------+
game_is_on = True
valid_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def check_winner_x():
    for combination in win_combinations:
        evaluate_combination = [grid[pos] for pos in combination]
        if '-' not in evaluate_combination and 'O' not in evaluate_combination and 'X' in grid:
            print('Player "X" has created a line across the board! They win!')
            return True


def check_winner_o():
    for combination in win_combinations:
        evaluate_combination = [grid[pos] for pos in combination]
        if '-' not in evaluate_combination and 'X' not in evaluate_combination and 'O' in grid:
            print('Player "O" has created a line across the board! They win!')
            return True


def play():
    playing = True
    while playing:
        x_won = check_winner_x()
        o_won = check_winner_o()
        if o_won or x_won:
            x_turn = False
            playing = False
        else:
            x_turn = True
        while x_turn:
            x_won = check_winner_x()
            if '-' not in grid or x_won or o_won:
                playing = False
                x_turn = False
            else:
                x_input = int(input('Enter a position for player "X": '))
                if x_input in valid_moves:
                    if grid[x_input - 1] == 'X' or grid[x_input - 1] == 'O':
                        print('That position has already been taken, please try again!')
                    else:
                        grid[x_input - 1] = 'X'
                        board = f'{grid[0:3]}\n{grid[3:6]}\n{grid[6:9]}\n'
                        print(board)
                        x_turn = False
                        x_won = check_winner_x()
                else:
                    print('Invalid input, please try again!')

        if o_won or x_won:
            o_turn = False
            playing = False
        else:
            o_turn = True
        while o_turn:
            o_won = check_winner_o()
            if '-' not in grid or x_won or o_won:
                playing = False
                o_turn = False
            else:
                o_input = int(input('Enter a position for player "O": '))
                if o_input in valid_moves:
                    if grid[o_input - 1] == 'X' or grid[o_input - 1] == 'O':
                        print('That position has already been taken, please try again!')
                    else:
                        grid[o_input - 1] = 'O'
                        board = f'{grid[0:3]}\n{grid[3:6]}\n{grid[6:9]}\n'
                        print(board)
                        o_turn = False
                else:
                    print('Invalid input, please try again!')


while game_is_on:
    grid = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
    win_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    play()

    ask_for_repeat = True
    while ask_for_repeat:
        repeat_prompt = input('Play again? Type "Y" for Yes, or "N" for No: ').lower()
        if repeat_prompt == 'y' or repeat_prompt == 'n':
            if repeat_prompt == 'n':
                print(thank_you)
                game_is_on = False
            ask_for_repeat = False
        else:
            print('Invalid input, please try again!')
