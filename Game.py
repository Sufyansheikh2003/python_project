import random as rd

import sys

print("****** Random Number Gusessing Game ******\n")

computer_number = rd.randint(1, 20)

lives = 3

while lives > 0:
    user_input = int(input("Enter Any Number between 1 and 20: "))

    if user_input == computer_number:
        print("You Won!")
        sys.exit()

    else: lives -= 1

    if user_input > computer_number:
        print("Hint: Think Lower Number")

    elif user_input < computer_number:
        print("Hint: Think Higher Number")

    if lives == 0:
        print("You Lose!")

    else:
        print(f"{lives} Remaining!")