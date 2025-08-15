from brain_games.engine import play_game  # type: ignore
from brain_games.games import even  # type: ignore


def main():
    play_game(even.get_question_and_answer, even.game_task)


if __name__ == '__main__':
    main()