import os

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def get_user_position(width, height):
    while True:
        position = input("Enter field position: ")
        try:
            if not position[0].isalpha() or not position[1].isnumeric():
                raise ValueError
            if int(position[1]) < 1 or int(position[1]) > height:
                raise ValueError
            letter = position[0].lower()
            column = ord(letter) - 97
            row = int(position[1])-1
            if not column < width:
                raise ValueError
        except ValueError:
            print("Position is wrong, try again!")
        return (row, column)

# clears the screen
def console_clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    # write your code here
    pass

if __name__ == "__main__":
    main()