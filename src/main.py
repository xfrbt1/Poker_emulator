import cProfile
import datetime
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

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
    print(f"|{pl_n}             |{n}        |{draws}    |{time}|")


print("PLAYERS AMOUNT |GAMES      |DRAWS      |TIME      ")


def main():
    for n in [1_0]:
        for pl_n in [2, 3, 4, 5, 6]:
            print("_______________________________________________________________")
            emulate_not_finish_version(n, pl_n)


if __name__ == '__main__':
    # Создаем объект cProfile.Profile
    profiler = cProfile.Profile()

    # Запускаем профилирование
    profiler.enable()

    # Вызываем вашу функцию
    main()

    # Останавливаем профилирование
    profiler.disable()

    # Выводим статистику профилирования
    profiler.print_stats(sort='cumulative')
