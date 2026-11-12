from random import randint

MIN_LENGTH = 5
MAX_LENGTH = 10
MIN_STEP = 1
MAX_STEP = 10
START_RANGE = (1, 50)
HIDDEN_MARKER = '..'


def make_progression(start, step, length):
    return [start + index * step for index in range(length)]


def generate_question():
    start = randint(*START_RANGE)
    step = randint(MIN_STEP, MAX_STEP)
    length = randint(MIN_LENGTH, MAX_LENGTH)

    progression = make_progression(start, step, length)
    hidden_index = randint(0, length - 1)

    elements = [str(number) for number in progression]
    correct_answer = elements[hidden_index]
    elements[hidden_index] = HIDDEN_MARKER

    question = ' '.join(elements)
    return question, correct_answer
