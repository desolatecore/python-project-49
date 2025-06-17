import random
from brain_games.cli import welcome_user

def main():
    from brain_games.scripts.brain_even import play_game
    play_game()

def is_even(number):
    return number % 2 == 0


def play_game():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers = 0

    while correct_answers < 3:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        answer = input('Your answer: ')
        if is_even(number):
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        if answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else: 
            print(f"{answer} is wrong answer ;(.") 
            print(f"Correct answer was {correct_answer}.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")