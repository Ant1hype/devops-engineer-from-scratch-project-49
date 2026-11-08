from brain_games.games import gcd
from brain_games.games.game_engine import play_games


def main():
    DESCRIPTION = 'Find the greatest common divisor of given numbers.'
    play_games(DESCRIPTION, gcd)


if __name__ == '__main__':
    main()
