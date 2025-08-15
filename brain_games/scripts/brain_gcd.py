from brain_games.engine import play_game
from brain_games.games import gcd


def main():
    play_game(gcd.get_question_and_answer, gcd.GAME_TASK)


if __name__ == '__main__':
    main()