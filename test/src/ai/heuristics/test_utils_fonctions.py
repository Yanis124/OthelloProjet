import sys
import os
current_dir = os.getcwd()

# Navigate to the parent directory
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../'))
sys.path.append(src_path)

from src.ai.heuristics.heuristique_utils_fonctions import circle_count, circle_count_corner, mobility 
from test_config import *

#test the circle count function when black is the max player board
def test_circle_count_black():
    
    max_player_color = 'black'
    min_player_color = 'white'
    expected_result_full_board = 32
    expected_result_initial_board = 0
    expected_result_random_board = 1  
    assert circle_count(state_full_board, max_player_color, min_player_color) == expected_result_full_board
    assert circle_count(state_initial_board, max_player_color, min_player_color) == expected_result_initial_board
    assert circle_count(state_random_board, max_player_color, min_player_color) == expected_result_random_board

#test the circle count function when white is the max player
def test_circle_count_white():
    
    max_player_color = 'white'
    min_player_color = 'black'
    expected_result_full_board = -32
    expected_result_initial_board = 0
    expected_result_random_board = -1  
    assert circle_count(state_full_board, max_player_color, min_player_color) == expected_result_full_board
    assert circle_count(state_initial_board, max_player_color, min_player_color) == expected_result_initial_board
    assert circle_count(state_random_board, max_player_color, min_player_color) == expected_result_random_board

#test the corner function when black is the max player
def test_circle_corner_black():

    max_player_color = 'black'
    min_player_color = 'white'
    expected_result_full_board = +2
    expected_result_initial_board = 0
    expected_result_random_board = +2  
    assert circle_count_corner(state_full_board, max_player_color, min_player_color) == expected_result_full_board
    assert circle_count_corner(state_initial_board, max_player_color, min_player_color) == expected_result_initial_board
    assert circle_count_corner(state_random_board, max_player_color, min_player_color) == expected_result_random_board

#test the corner function when white is the max player
def test_circle_corner_white():

    max_player_color = 'white'
    min_player_color = 'black'
    expected_result_full_board = -2
    expected_result_initial_board = 0
    expected_result_random_board = -2  
    assert circle_count_corner(state_full_board, max_player_color, min_player_color) == expected_result_full_board
    assert circle_count_corner(state_initial_board, max_player_color, min_player_color) == expected_result_initial_board
    assert circle_count_corner(state_random_board, max_player_color, min_player_color) == expected_result_random_board

#test the mobility function when black is the max player
def test_mobility_black():
    pass

#test the mobility function when white is the max player
def test_mobility_white():
    pass

#test the stability function when black is the max player
def test_stability_black():
    pass

#test the stability function when white is the max player
def test_stability_white():
    pass
    
   
    

    
    
    


