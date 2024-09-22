import random

rand = random.randint(1,100)

attempts = 0
game_over = False
while not game_over:
    number = int(input("Enter a number from 1 to 100: "));
    attempts += 1
    if number < rand :
        print("Try Higher!")
    if number > rand:
        print("Try Lower!")
    if number == rand:
        print("You Win!!")
        print(f"You guessed in {attempts} attempts.")
