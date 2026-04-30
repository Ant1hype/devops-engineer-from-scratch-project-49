from random import randint

from brain_games.games.start_end import END_RANDOM_RANGE, START_RANDOM_RANGE


def is_even(number):
    return number % 2 == 0


def generate_question():
    number = randint(START_RANDOM_RANGE, END_RANDOM_RANGE)
    correct_answer = "yes" if is_even(number) else "no"
    return number, correct_answer