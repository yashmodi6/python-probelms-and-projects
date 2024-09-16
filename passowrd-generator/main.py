# This is not a practical password generator as random module is pseudo random
# Nor i am forcing any kind of rules for password to follow

import random


def gen_password(length) -> str:
    charset_lower = "abcdefghijklmnopqrstuvwxyz"
    charset_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number = "0123456789"
    symbols = """!@#$%^&*()_+{}"|:?><[]';/.,'"""

    password = ""
    for _ in range(length):
        rchar = random.choice(charset_lower + charset_upper + number + symbols)
        password += rchar

    return password


# this function is not necessary but was made for my own sanity
def main():
    length = int(input("Enter password length: "))
    password = gen_password(length)
    print(password)


if __name__ == "__main__":
    main()
