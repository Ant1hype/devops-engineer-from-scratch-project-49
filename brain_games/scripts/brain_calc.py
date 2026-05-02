from brain_games.games import calc
from brain_games.games.game_engine import play_games


def main():
    DESCRIPTION = 'What is the result of the expression?'
    play_games(DESCRIPTION, calc)


if __name__ == '__main__':
    main()