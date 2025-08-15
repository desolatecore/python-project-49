ROUNDS_COUNT = 3


def play_game(get_question_and_answer, game_task):
    from brain_games.cli import welcome_user

    name = welcome_user()
    print(game_task)

    for _ in range(ROUNDS_COUNT):
        question, correct_answer = get_question_and_answer()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")

        if user_answer != str(correct_answer):
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")  # noqa: E501
            print(f"Let's try again, {name}!")
            return

        print("Correct!")

    print(f"Congratulations, {name}!")