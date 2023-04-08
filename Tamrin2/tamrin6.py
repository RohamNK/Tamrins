import random

print("Welcome to dice! To roll, enter 'roll'. To quit, enter 'exit'.")

while True:
    op = input("Enter your choice: ")

    if op == "roll":
        sel = random.randint(1, 6)
        if sel < 6:
            print("Game is up! You rolled:", sel)
            print("Starting over. To roll, enter 'roll'. To quit, enter 'exit'.")
        else:
            print("You won! The roll was", sel, "! You can roll again by entering 'roll'.")
    elif op == "exit":
        break
    else:
        print("Invalid input. Please enter 'roll' to roll the dice or 'exit' to quit.")
