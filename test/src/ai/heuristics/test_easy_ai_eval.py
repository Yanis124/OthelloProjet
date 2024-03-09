import pytest
import sys
import os
current_dir = os.getcwd()

# Naviage to the src folder 
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../'))
sys.path.append(src_path)
print(src_path)

from src.ai.heuristics.easy_ai_eval import easy_ai_utility  # Import your function
from test_config import *

#test the easy_ai function with black as max player
def test_easy_ai_eval__black():
    
    max_player_color = 'black'
    min_player_color = 'white'
    expected_result_full_board = 32
    expected_result_initial_board = 0
    expected_result_random_board = 1  
    assert easy_ai_utility(state_full_board, max_player_color, min_player_color) == expected_result_full_board
    assert easy_ai_utility(state_initial_board, max_player_color, min_player_color) == expected_result_initial_board
    assert easy_ai_utility(state_random_board, max_player_color, min_player_color) == expected_result_random_board

#test the easy_ai function with white as max player
def test_easy_ai_eval_white():

    max_player_color = 'white'
    min_player_color = 'black'
    expected_result_full_board = -32
    expected_result_initial_board = 0
    expected_result_random_board = -1
    assert easy_ai_utility(state_full_board, max_player_color, min_player_color) == expected_result_full_board
    assert easy_ai_utility(state_initial_board, max_player_color, min_player_color) == expected_result_initial_board
    assert easy_ai_utility(state_random_board, max_player_color, min_player_color) == expected_result_random_board

