import random


def generate_secret_number():
    digits = list("0123456789")
    random.shuffle(digits)
    # Ensure the first digit isn't '0'
    if digits[0] == "0":
        digits[0], digits[1] = digits[1], digits[0]
    return "".join(digits[:4])


def get_cows_and_bulls(secret, guess):

    bulls = 0
    cows = 0

    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1

    return cows, bulls


def play_game():
    print("Welcome to Cows and Bulls!")
    print("Try to guess the 4-digit secret number (unique digits).")

    secret_number = generate_secret_number()
    attempts = 0

    while True:
        guess = input("\nEnter your 4-digit guess: ").strip()

        # Validation: Must be 4 digits, all numbers, all unique
        if len(guess) != 4 or not guess.isdigit() or len(set(guess)) != 4:
            print("Invalid input! Please enter exactly 4 unique digits.")
            continue

        attempts += 1
        cows, bulls = get_cows_and_bulls(secret_number, guess)

        if bulls == 4:
            print(f"\n🎉 Congratulations! You guessed it in {attempts} attempts!")
            print(f"The number was indeed {secret_number}.")
            break
        else:
            print(f"🐂 Bulls (Correct position): {bulls}")
            print(f"🐄 Cows (Wrong position): {cows}")


if __name__ == "__main__":
    play_game()
