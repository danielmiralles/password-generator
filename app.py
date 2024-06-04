# letters
# 97 - 122 and 65 - 90
import string
from random import choice, randint


# symbols 33 - 43


def generate_password(letter_cnt, number_cnt, symbol_cnt):
    password_list = []
    total_size = letter_cnt + number_cnt + symbol_cnt
    for i in range(total_size):
        letter = choice(string.ascii_letters)
        number = choice(string.digits)
        symbol = chr(randint(33, 44))
        choices = []
        if letter_cnt > 0:
            choices.append(letter)
        if number_cnt > 0:
            choices.append(number)
        if symbol_cnt > 0:
            choices.append(symbol)
        to_insert = choice(choices)
        if to_insert == letter:
            letter_cnt -= 1
        elif to_insert == number:
            number_cnt -= 1
        else:
            symbol_cnt -= 1
        password_list.append(to_insert)
    return "".join(password_list)


print("Welcome to Password Generator!")
letter_count = int(input("How many letters would you like in your password? "))
number_count = int(input("How many numbers would you like in your password? "))
symbol_count = int(input("How many symbols would you like in your password? "))
password = generate_password(letter_count, number_count, symbol_count)
print(f"Your password is: {password}")
