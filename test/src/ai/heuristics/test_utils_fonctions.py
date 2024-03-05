import pytest
import sys
import os
current_dir = os.getcwd()

# Navigate to the parent directory
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../'))
sys.path.append(src_path)

from src.ai.heuristics.utils_fonctions import circle_count  # Import your function
from test_config import *

def test_circle_count_black_full_board():
    
    max_player_color = 'black'
    min_player_color = 'white'
    expected_result = 32  
    assert circle_count(state_full_board, max_player_color, min_player_color) == expected_result

def test_circle_count_white_full_board():

    max_player_color = 'white'
    min_player_color = 'black'
    expected_result = -32  
    assert circle_count(state_full_board, max_player_color, min_player_color) == expected_result
    
def test_circle_count_black_initial_board():

    max_player_color = 'black'
    min_player_color = 'white'
    expected_result = 0  
    assert circle_count(state_initial_board, max_player_color, min_player_color) == expected_result
    
def test_circle_count_white_initial_board():

    max_player_color = 'white'
    min_player_color = 'black'
    expected_result = 0  
    assert circle_count(state_initial_board, max_player_color, min_player_color) == expected_result

def test_circle_count_black_random_board():

    max_player_color = 'black'
    min_player_color = 'white'
    expected_result = 1  
    assert circle_count(state_random_board, max_player_color, min_player_color) == expected_result
        
def test_circle_count_white_random_board():

    max_player_color = 'white'
    min_player_color = 'black'
    expected_result = -1
    assert circle_count(state_random_board, max_player_color, min_player_color) == expected_result
    


