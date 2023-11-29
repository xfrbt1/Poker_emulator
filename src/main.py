import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from src.game_state.game_state import GameState
from src.game_state.combination_analyzer import Analyzer

# game_state = GameState(2)
#
# for i in range(10):
#     game_state.update()
#     game_state.analyze()
#     print("\n")

