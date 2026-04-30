from brain_games.games import even
from brain_games.games.game_engine import play_games


def main():
    DESCRIPTON = 'Answer "yes" if the number is even, otherwise answer "no".'
    play_games(DESCRIPTON, even)


if __name__ == "__main__":
    main()