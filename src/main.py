import datetime

from src.game_state.game_state import GameState


def emulate_not_finish_version(n, pl_n):
    game_state = GameState(pl_n)
    start = datetime.datetime.now()

    for i in range(n):
        game_state.update()
        game_state.analyze()

    end = datetime.datetime.now()
    draws = game_state.draws
    time = end - start

    print(f"|players: {pl_n}|games: {n}|same comb: {draws}|time: {time}|")


def main(pl_n):
    for n in [100, 1000, 10000]:
        print("_______________________________________________________________")
        emulate_not_finish_version(n, pl_n)


if __name__ == "__main__":
    main(2)
