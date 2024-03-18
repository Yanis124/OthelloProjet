import sys
import os
current_dir = os.getcwd()

# Naviage to the src folder 
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../'))
sys.path.append(src_path)
print(src_path)

from src.ai.heuristics.hard_ai_eval import hard_ai_utility, calculate_heuristique_score  # Import your function
from test_config import *

#test the calculate_heuristique_score if it return the correct score
def test_calculate_heuristique_score_parametres_not_zero():
    
    max_player_parametre = -5
    min_player_parametre = -2
    
    expected_result = -300/7
    
    assert calculate_heuristique_score(max_player_parametre, min_player_parametre) == expected_result
    
     

#test the calculate_heuristique_score if it return 0 if both score are 0
def test_calculate_heuristique_score_parametres_zero():
    
    max_player_parametre = 0
    min_player_parametre = 0
    
    expected_result = 0
    
    assert calculate_heuristique_score(max_player_parametre, min_player_parametre) == expected_result
    
#test the hard_ai_utility when black is the max_player
def test_hard_ai_utility_black():
    
    max_player_color = "black"
    min_player_color = "white"
    
    expected_result_full_board = 50
    expected_result_initial_board = 0
    expected_result_random_board = (100 / 51) + 50 + (-900 / 7) 
     
    assert hard_ai_utility(state_full_board, max_player_color, min_player_color) == expected_result_full_board
    assert hard_ai_utility(state_initial_board, max_player_color, min_player_color) == expected_result_initial_board
    assert hard_ai_utility(state_random_board, max_player_color, min_player_color) == expected_result_random_board
    
def test_hard_ai_utility_white():
    
    max_player_color = "white"
    min_player_color = "black"
    
    expected_result_full_board = -50
    expected_result_initial_board = 0
    expected_result_random_board = (-100 / 51) + (-50) + (900 / 7) 
     
    assert hard_ai_utility(state_full_board, max_player_color, min_player_color) == expected_result_full_board
    assert hard_ai_utility(state_initial_board, max_player_color, min_player_color) == expected_result_initial_board
    assert hard_ai_utility(state_random_board, max_player_color, min_player_color) == expected_result_random_board
