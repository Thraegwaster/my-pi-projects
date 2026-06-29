import random
battle_pattern=[]
for i in range(5):
    battle_pattern.append(['O '] * 5)

def display(pattern):
    for p in pattern:
        print(" ".join(p))

print("Let's play Battleship!")
display(battle_pattern)
def get_random_row(pattern):
    return random.randint(0, len(pattern) - 1)

def get_random_col(pattern):
    return random.randint(0, len(pattern[0]) - 1)

ship_row = get_random_row(battle_pattern)
ship_col = get_random_col(battle_pattern)

print(f"hint: row={ship_row}, col={ship_col}")

for option in range(4):
    input_row=int(input("Enter guess row (starts with 0):"))
    input_col=int(input("Enter guess col (starts with 0):"))
    if input_row == ship_row and input_col == ship_col:
        print("Congratulations! You sunk my battleship!")
        break
    else:
        if option == 3:
            battle_pattern[input_row][input_col] = 'X '
            display(battle_pattern)
            print("Game Over")
            print("\nShip is here:["+str(ship_row)+"]["+str(ship_col)+"]")
        else:
            if (input_row < 0 or input_row > 4) or (input_col < 0 or input_col > 4):
                print("Oops, that's not even in the ocean.")
            elif (battle_pattern[input_row][input_col] == 'X '):
                print("You guessed that one already.")
            else:
                print("You missed my battleship!")
                battle_pattern[input_row][input_col] = 'X '
                print("Attempt: ",option+1)
                display(battle_pattern)