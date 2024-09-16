import random

# Blueprint for making the game
# 1. Pick a word
# 2. Show blanks
# 3. Get a letter
# 4. Check the letter (guessed or wrong or invalid)
# 5. Reveal it if correct
# 6. Count mistakes
# 7. Check for win
# 8. Check for loss
# 9. Ask to play again

hangman_art = [
    # 0 - No mistakes
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    # 1 - Head
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    # 2 - Head + body
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    # 3 - Add left arm
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    # 4 - Add right arm
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    # 5 - Add left leg
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
         |
    =========
    """,
    # 6 - Final stage
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
         |
    =========
    """,
]


def get_random_word() -> str:
    file_path = "hangman/words.txt"

    with open(file_path, "r") as file:
        lines = file.readlines()

    return random.choice(lines).strip().lower()


def is_valid_guess(ch: str) -> bool:
    return len(ch) == 1 and ch.isalpha()


def display_word(word, guessed_indices):
    for i in range(len(word)):
        if i in guessed_indices:
            print(word[i], end="")
        else:
            print("_", end="")
    print()


def is_word_guessed(word, guessed_indices) -> bool:
    return len(guessed_indices) == len(word)


max_wrong = 6

wants_to_continue = True

while wants_to_continue:
    # Reset everything for a new game
    wrong_guess = 0
    guessed_indices = []
    guessed_letters = []

    r_word = get_random_word()

    print("\n=== HANGMAN ===")

    while wrong_guess < max_wrong:
        print(hangman_art[wrong_guess])
        display_word(r_word, guessed_indices)

        guess = input("Enter a character to guess: ").lower()

        # Validate input
        if not is_valid_guess(guess):
            print("Please enter exactly one alphabetic character.")
            continue

        # Check if already guessed
        if guess in guessed_letters:
            print("You already guessed that character.")
            continue

        guessed_letters.append(guess)

        # Wrong guess
        if guess not in r_word:
            wrong_guess += 1
            print(f"Wrong guess! Attempts remaining: {max_wrong - wrong_guess}")
            continue

        # Correct guess
        for i in range(len(r_word)):
            if r_word[i] == guess:
                guessed_indices.append(i)

        print("Correct guess!")

        # Check if the entire word has been guessed
        if is_word_guessed(r_word, guessed_indices):
            print(hangman_art[wrong_guess])
            display_word(r_word, guessed_indices)
            print("You won!")
            break

    # Player lost
    if wrong_guess == max_wrong:
        print(hangman_art[wrong_guess])
        print(f"You lost! The word was: {r_word}")

    # Play again?
    while True:
        ch = input("Do you want to play again (y/n)? ").lower()

        if ch == "y":
            wants_to_continue = True
            break
        elif ch == "n":
            wants_to_continue = False
            break
        else:
            print("Please enter 'y' or 'n'.")
            wants_to_continue = False
            break

print("Thanks for playing!")
