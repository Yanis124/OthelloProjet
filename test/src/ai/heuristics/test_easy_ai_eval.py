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


def test_easy_ai_eval__black_full_board():
    
    max_player_color = 'black'
    min_player_color = 'white'
    expected_result = 32  
    assert easy_ai_utility(state_full_board, max_player_color, min_player_color) == expected_result

def test_easy_ai_eval_white_full_board():

    max_player_color = 'white'
    min_player_color = 'black'
    expected_result = -32  
    assert easy_ai_utility(state_full_board, max_player_color, min_player_color) == expected_result
    
def test_easy_ai_eval_black_initial_board():

    max_player_color = 'black'
    min_player_color = 'white'
    expected_result = 0
    assert easy_ai_utility(state_initial_board, max_player_color, min_player_color) == expected_result
    
def test_easy_ai_eval_white_initial_board():

    max_player_color = 'white'
    min_player_color = 'black'
    expected_result = 0  
    assert easy_ai_utility(state_initial_board, max_player_color, min_player_color) == expected_result
    
def test_easy_ai_eval_black_random_board():

    max_player_color = 'black'
    min_player_color = 'white'
    expected_result = 1  
    assert easy_ai_utility(state_random_board, max_player_color, min_player_color) == expected_result
        
def test_easy_ai_eval_white_random_board():

    max_player_color = 'white'
    min_player_color = 'black'
    expected_result = -1
    assert easy_ai_utility(state_random_board, max_player_color, min_player_color) == expected_result

