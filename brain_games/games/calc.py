import operator
import random

game_task = "What is the result of the expression?"


def get_question_and_answer():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }
    op = random.choice(list(operations.keys()))
    question = f'{num1} {op} {num2}'
    answer = operations[op](num1, num2)
    return question, answer
