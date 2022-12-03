import os
import random

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def generate_board(height, width):
    board = []
    amount_of_letters = int((height*width) / 2)
    letters_on_board = dict()
    try:
        if ((height*width) % 2 != 0) or (amount_of_letters > len(alphabet)):
            raise ValueError
        for _ in range(amount_of_letters):
            letter = random.choice(alphabet)
            while letter in letters_on_board:
                letter = random.choice(alphabet)  
            letters_on_board[letter] = 2
        for col in range(width):
            column = []
            for row in range(height):
                current_letter = random.choice(list(letters_on_board.keys()))
                column.append(current_letter)
                letters_on_board[current_letter] -= 1
                if letters_on_board[current_letter] == 0:
                    del letters_on_board[current_letter]
            board.append(column)
            print(column)
    except ValueError:
        print("Unable to generate the board")
    return board

# clears the screen
def console_clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    # write your code here
    pass

if __name__ == "__main__":
    main()