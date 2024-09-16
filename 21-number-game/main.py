# 21 Number Game (also known as Bagram or Twenty Plus One) is a counting game
# in which players take turns to count numbers from 1 to 21.
# The player who calls "21" loses the game
# This program implements a Player vs Computer version for it

import random


# Prints rule of the games
def intro():
    print("""
              21 NUMBER GAME
              --------------

    HOW TO PLAY

    • Take turns with the computer.
    • Say 1, 2, or 3 consecutive numbers on your turn.
    • Numbers must continue in order.
    • The game starts at 1.
    • Whoever says 21 loses.

    Example:
      You → 1 2
      Computer → 3 4 5
      You → 6
      Computer → 7 8

              Let's begin!
    """)


# Generate 1 to 3 consecutive numbers for the computer
def get_computer_choices(number_sequence: list[int]):
    computer_input = random.randint(1, 3)
    computer_guess = []

    for i in range(1, computer_input + 1):
        next_number = number_sequence[-1] + i

        # Stop if the next number goes beyond 21
        if next_number > 21:
            break

        computer_guess.append(next_number)

    return computer_guess


# Check whether the player's numbers continue the sequence
def is_valid_sequence(user_input, number_sequence):

    # The first number of the game must be 1
    if not number_sequence:
        if user_input[0] != 1:
            return False

    # Make sure the first number follows the previous number
    elif user_input[0] != number_sequence[-1] + 1:
        return False

    # Make sure all numbers entered by the player are consecutive
    for i in range(1, len(user_input)):
        if user_input[i] != user_input[i - 1] + 1:
            return False

    return True


# Check whether the player's input contains 1 to 3 valid numbers
def is_valid_input(user_input):

    if not 0 < len(user_input) <= 3:
        return False

    # Only numbers from 1 to 21 are allowed
    for item in user_input:
        if not 1 <= item <= 21:
            return False

    return True


# Ask the player whether they want to play another game
def play_again():
    while True:
        ch = input("Do you want to play again (y/n)? ").lower()

        if ch == "y":
            return True
        elif ch == "n":
            return False
        else:
            print("Please enter 'y' or 'n'.")


# Check if a player has said 21
def lost(sequence):
    return 21 in sequence


wants_to_continue = True

# Keep starting new games until the player chooses to stop
while wants_to_continue:
    number_sequence = []
    intro()
    # Continue taking turns in the current game
    while True:
        user_input = []

        # Convert the player's input into a list of integers
        try:
            user_input = input("Player says: ").split()
            user_input = [int(x) for x in user_input]
        except ValueError:
            print("Please enter numbers only.")
            continue

        # Reject invalid input
        if not is_valid_input(user_input):
            print("You can only enter three numbers and from 1 to 21 only!!")
            continue

        # Reject numbers that don't continue the sequence
        if not is_valid_sequence(user_input, number_sequence):
            print("Numbers entered are not in valid sequence!!")
            print("Player Lost!!")
            wants_to_continue = play_again()
            break

        # The player loses if they say 21
        if lost(user_input):
            print("Player Lost!!")
            wants_to_continue = play_again()
            break

        # Add the player's numbers to the game sequence
        number_sequence.extend(user_input)

        # Generate the computer's numbers
        computer_guess = get_computer_choices(number_sequence)

        # Add the computer's numbers to the game sequence
        number_sequence.extend(computer_guess)

        print("Computer says: ", end="")
        print(*computer_guess)

        # The computer loses if it says 21
        if lost(computer_guess):
            print("Computer Lost!!")
            wants_to_continue = play_again()
            break
