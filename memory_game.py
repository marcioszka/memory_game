import os
from random import randint

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
difficulties = {'easy': (5,4), 'medium': (5,6), "hard": (5,10)}

# clears the screen
def console_clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_difficulties():
    difficulties_names = [*difficulties.keys()]
    print('Choose difficulty:')
    for name in difficulties_names:
        print(f'    {name.upper()[0]+name.lower()[1:]}')


def get_difficulty_level():
    chosen = False
    while not chosen:
        print_difficulties()
        choice = input('Your choice is: ')
        if choice.lower() in difficulties.keys():
            chosen = True
        else:
            print('\nThere is no sush difficulty level!',end='\n\n')
    return choice.lower()


def get_shown_board(width, height):
    return [[False for _ in range(height)] for _ in range(width)]


def draw_board(board, shown_board, coordinates = None):
    print('\n  ',end='')
    for i in range(len(board)):
        print(f'{alphabet[i]} ', end='')
    print()
    for i in range(len(board[0])):
        print(f'{i+1} ',end='')
        for j in range(len(board)):
            character = '#'
            if coordinates != None:
                if coordinates[0] == j and coordinates [1] == i:
                    character = board[j][i]
            if shown_board[j][i]:
                character = board[j][i]
            print(f'{character} ',end='')
        print()
    print()


def main():
    steps = 0
    print('\nWelcome to Memory Game!',end='\n\n')
    size = difficulties[get_difficulty_level()]
    board = [['A','B','C','D'],['E','F','G','H'],['E','F','G','H'],['I','J','J','I'],['A','B','C','D']] # Get board
    shown_board = get_shown_board(len(board), len(board[0]))
    draw_board(board,shown_board)
    end = False
    while not end:
        first_coords = (randint(0, len(board)-1), randint(0,len(board[0])-1)) # input
        console_clear()
        draw_board(board,shown_board,first_coords)
        second_coords = (randint(0, len(board)-1), randint(0,len(board[0])-1)) # input
        if board[first_coords[0]][first_coords[1]] == board[second_coords[0]][second_coords[1]]:
            shown_board[first_coords[0]][first_coords[1]] = True
            shown_board[second_coords[0]][second_coords[1]] = True
        console_clear()
        steps += 1
        draw_board(board,shown_board,second_coords)
        if False not in [cell for col in shown_board for cell in col]:
            end = True
    print(f'Congratulations! You\'ve finished the game in : {steps} steps.')

if __name__ == "__main__":
    main()