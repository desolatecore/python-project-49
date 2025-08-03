import random


GAME_TASK = "What number is missing in the progression?"


def get_question_and_answer():
    length = random.randint(5, 10)
    start = random.randint(1, 50)
    step = random.randint(1, 10)

    progression = [start + i * step for i in range(length)]
    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = ".."

    question = " ".join(str(x) for x in progression)
    return question, str(correct_answer)