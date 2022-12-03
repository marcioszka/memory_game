import os

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
    print('  ',end='')
    for i in range(len(board)):
        print(f'{i+1} ', end='')
    print()
    for i in range(len(board[0])):
        print(f'{alphabet[i]} ',end='')
        for j in range(len(board)):
            character = '#'
            if coordinates != None:
                if coordinates[0] == j and coordinates [1] == i:
                    character = board[j][i]
            if shown_board[j][i]:
                character = board[j][i]
            print(f'{character} ',end='')
        print()



def main():
    pass


if __name__ == "__main__":
    main()