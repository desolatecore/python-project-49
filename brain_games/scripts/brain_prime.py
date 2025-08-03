from brain_games.engine import play_game  # type: ignore
from brain_games.games import prime  # type: ignore


def main():
    play_game(prime.get_question_and_answer, prime.GAME_TASK)


if __name__ == '__main__':
    main()
