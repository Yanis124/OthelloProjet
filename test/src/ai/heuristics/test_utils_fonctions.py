import pytest
import sys
import os
current_dir = os.getcwd()

# Navigate to the parent directory
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../'))
sys.path.append(src_path)

from src.ai.heuristics.utils_fonctions import circle_count, circle_count_corner, mobility # Import your function
from test_config import *

def test_circle_count_black():
    """test the circle count function with a full board"""
    
    max_player_color = 'black'
    min_player_color = 'white'
    expected_result_full_board = 32
    expected_result_initial_board = 0
    expected_result_random_board = 1  
    assert circle_count(state_full_board, max_player_color, min_player_color) == expected_result_full_board
    assert circle_count(state_initial_board, max_player_color, min_player_color) == expected_result_initial_board
    assert circle_count(state_random_board, max_player_color, min_player_color) == expected_result_random_board

def test_circle_count_white():
    """test the circle count function with a full board"""
    
    max_player_color = 'white'
    min_player_color = 'black'
    expected_result_full_board = -32
    expected_result_initial_board = 0
    expected_result_random_board = -1  
    assert circle_count(state_full_board, max_player_color, min_player_color) == expected_result_full_board
    assert circle_count(state_initial_board, max_player_color, min_player_color) == expected_result_initial_board
    assert circle_count(state_random_board, max_player_color, min_player_color) == expected_result_random_board
    
def test_circle_count_black():

    max_player_color = 'black'
    min_player_color = 'white'
    expected_result_full_board = +2
    expected_result_initial_board = 0
    expected_result_random_board = +2  
    assert circle_count_corner(state_full_board, max_player_color, min_player_color) == expected_result_full_board
    assert circle_count_corner(state_initial_board, max_player_color, min_player_color) == expected_result_initial_board
    assert circle_count_corner(state_random_board, max_player_color, min_player_color) == expected_result_random_board
    
def test_circle_count_black():

    max_player_color = 'white'
    min_player_color = 'black'
    expected_result_full_board = -2
    expected_result_initial_board = 0
    expected_result_random_board = -2  
    assert circle_count_corner(state_full_board, max_player_color, min_player_color) == expected_result_full_board
    assert circle_count_corner(state_initial_board, max_player_color, min_player_color) == expected_result_initial_board
    assert circle_count_corner(state_random_board, max_player_color, min_player_color) == expected_result_random_board
    
def test_mobility_black():
    
    max_player_color = 'black'
    min_player_color = 'white'
    current_player_color = 'black'
    expected_result_empty = 0
    expected_result_random = 4
    assert mobility(available_moves_random, current_player_color, max_player_color, min_player_color) == expected_result_random
    assert mobility(available_moves_empty, max_player_color, max_player_color, min_player_color) == expected_result_empty
    
def test_mobility_black():
    
    max_player_color = 'black'
    min_player_color = 'white'
    current_player_color = 'white'
    expected_result_empty = 0
    expected_result_random = -4
    assert mobility(available_moves_random, current_player_color, max_player_color, min_player_color) == expected_result_random
    assert mobility(available_moves_empty, current_player_color, max_player_color, min_player_color) == expected_result_empty
    

    
    
    


