from brain_games.engine import play_game  # type: ignore
from brain_games.games import calc  # type: ignore


def main():
    play_game(calc.get_question_and_answer, calc.game_task)


if __name__ == '__main__':
    main()