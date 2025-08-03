from brain_games.engine import play_game  # type: ignore
from brain_games.games import progression  # type: ignore


def main():
    play_game(progression.get_question_and_answer, progression.GAME_TASK)


if __name__ == '__main__':
    main()