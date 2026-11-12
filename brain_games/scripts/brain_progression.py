from brain_games.games import progression
from brain_games.games.game_engine import play_games


def main():
    DESCRIPTION = 'What number is missing in the progression?'
    play_games(DESCRIPTION, progression)


if __name__ == '__main__':
    main()
