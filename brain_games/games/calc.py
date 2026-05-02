from random import choice, randint

from brain_games.games.constants import START_RANDOM_RANGE, END_RANDOM_RANGE, OPERATORS


def generate_question():
    number_1 = randint(START_RANDOM_RANGE, END_RANDOM_RANGE)
    number_2 = randint(START_RANDOM_RANGE, END_RANDOM_RANGE)
    operator = choice(OPERATORS)

    question = f"{number_1} {operator} {number_2}"
    correct_answer = str(calc(number_1, number_2, operator))
    
    return question, correct_answer


def calc(number_1, number_2, operator):
    match operator:
        case '+':
            return number_1 + number_2
        case '-':
            return number_1 - number_2
        case '*':
            return number_1 * number_2