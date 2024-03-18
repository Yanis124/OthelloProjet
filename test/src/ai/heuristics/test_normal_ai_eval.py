import sys
import os
current_dir = os.getcwd()

# Navigate to the parent directory
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../'))
sys.path.append(src_path)

from src.ai.heuristics.normal_ai_eval import normal_ai_utility
from test_config import *

#test the normal ai eval function when black is the max player
def test_easy_ai_eval__black():
    
    max_player_color = 'black'
    min_player_color = 'white'
    expected_result_full_board = 0
    expected_result_initial_board = 0
    expected_result_random_board = 13
    assert normal_ai_utility(state_full_board, max_player_color, min_player_color) == expected_result_full_board
    assert normal_ai_utility(state_initial_board, max_player_color, min_player_color) == expected_result_initial_board
    assert normal_ai_utility(state_random_board, max_player_color, min_player_color) == expected_result_random_board
    
#test the normal ai eval function when white is the max player
def test_easy_ai_eval__white():
    
    max_player_color = 'white'
    min_player_color = 'black'
    expected_result_full_board = 0
    expected_result_initial_board = 0
    expected_result_random_board = -13
    assert normal_ai_utility(state_full_board, max_player_color, min_player_color) == expected_result_full_board
    assert normal_ai_utility(state_initial_board, max_player_color, min_player_color) == expected_result_initial_board
    assert normal_ai_utility(state_random_board, max_player_color, min_player_color) == expected_result_random_board