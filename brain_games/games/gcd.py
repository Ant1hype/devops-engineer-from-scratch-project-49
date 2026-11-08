from random import randint

from brain_games.games.constants import END_RANDOM_RANGE, START_RANDOM_RANGE


def gcd(number_1, number_2):
    while number_2:
        number_1, number_2 = number_2, number_1 % number_2
    return number_1


def generate_question():
    number_1 = randint(START_RANDOM_RANGE, END_RANDOM_RANGE)
    number_2 = randint(START_RANDOM_RANGE, END_RANDOM_RANGE)

    question = f"{number_1} {number_2}"
    correct_answer = str(gcd(number_1, number_2))

    return question, correct_answer
