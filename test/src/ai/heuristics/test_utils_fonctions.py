import sys
import os
current_dir = os.getcwd()

# Navigate to the parent directory
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../'))
sys.path.append(src_path)

from src.ai.heuristics.heuristique_utils_fonctions import circle_count, circle_count_corner, mobility, stability, is_stable, controlled_central_squares
from test_config import *

#test the circle count function when black is the max player board
def test_circle_count_black():
    
    max_player_color = 'black'
    min_player_color = 'white'
    expected_result_full_board = [48, 16]
    expected_result_initial_board = [2, 2]
    expected_result_random_board = [26, 25]
    assert circle_count(state_full_board, max_player_color, min_player_color) == expected_result_full_board
    assert circle_count(state_initial_board, max_player_color, min_player_color) == expected_result_initial_board
    assert circle_count(state_random_board, max_player_color, min_player_color) == expected_result_random_board

#test the circle count function when white is the max player
def test_circle_count_white():
    
    max_player_color = 'white'
    min_player_color = 'black'
    expected_result_full_board = [16, 48]
    expected_result_initial_board = [2, 2]
    expected_result_random_board = [25, 26]
    assert circle_count(state_full_board, max_player_color, min_player_color) == expected_result_full_board
    assert circle_count(state_initial_board, max_player_color, min_player_color) == expected_result_initial_board
    assert circle_count(state_random_board, max_player_color, min_player_color) == expected_result_random_board

#test the corner function when black is the max player
def test_circle_corner_black():

    max_player_color = 'black'
    min_player_color = 'white'
    expected_result_full_board = [3, 1]
    expected_result_initial_board = [0, 0]
    expected_result_random_board = [3, 1]
    assert circle_count_corner(state_full_board, max_player_color, min_player_color) == expected_result_full_board
    assert circle_count_corner(state_initial_board, max_player_color, min_player_color) == expected_result_initial_board
    assert circle_count_corner(state_random_board, max_player_color, min_player_color) == expected_result_random_board

#test the corner function when white is the max player
def test_circle_corner_white():

    max_player_color = 'white'
    min_player_color = 'black'
    expected_result_full_board = [1, 3]
    expected_result_initial_board = [0, 0]
    expected_result_random_board = [1, 3] 
    assert circle_count_corner(state_full_board, max_player_color, min_player_color) == expected_result_full_board
    assert circle_count_corner(state_initial_board, max_player_color, min_player_color) == expected_result_initial_board
    assert circle_count_corner(state_random_board, max_player_color, min_player_color) == expected_result_random_board

#test the mobility function when black is the max player
def test_mobility_black():
    
    max_player_color = 'black'
    min_player_color = 'white'
    expected_result_full_board = [0, 0]
    expected_result_initial_board = [4, 4]
    expected_result_random_board = [10, 10] 
    assert mobility(state_full_board, max_player_color, min_player_color) == expected_result_full_board
    assert mobility(state_initial_board, max_player_color, min_player_color) == expected_result_initial_board
    assert mobility(state_random_board, max_player_color, min_player_color) == expected_result_random_board

#test the mobility function when white is the max player
def test_mobility_white():
    
    max_player_color = 'white'
    min_player_color = 'black'
    expected_result_full_board = [0, 0]
    expected_result_initial_board = [4, 4]
    expected_result_random_board = [10, 10] 
    assert mobility(state_full_board, max_player_color, min_player_color) == expected_result_full_board
    assert mobility(state_initial_board, max_player_color, min_player_color) == expected_result_initial_board
    assert mobility(state_random_board, max_player_color, min_player_color) == expected_result_random_board

#test the function that check if a piece is stable for corner
def test_is_stable_corner():
    
    player = 'black'
    
    #full board
    assert is_stable(state_full_board, player, 7, 7) == False 
    assert is_stable(state_full_board, player, 0, 0) == True 
    assert is_stable(state_full_board, player, 0, 7) == True 
    assert is_stable(state_full_board, player, 7, 0) == True
     
    #start board
    assert is_stable(state_initial_board, player, 7, 7) == False 
    assert is_stable(state_initial_board, player, 0, 0) == False  
    assert is_stable(state_initial_board, player, 0, 7) == False  
    assert is_stable(state_initial_board, player, 7, 0) == False
    
    #start board
    assert is_stable(state_random_board, player, 7, 7) == True
    assert is_stable(state_random_board, player, 0, 0) == True  
    assert is_stable(state_random_board, player, 0, 7) == True  
    assert is_stable(state_random_board, player, 7, 0) == False
    
#test the function that check if a piece is stable for boundaries
def test_is_stable_boundaries():
    
    player = 'black'
    
    #full board
    assert is_stable(state_full_board, player, 0, 1) == True 
    assert is_stable(state_full_board, player, 0, 2) == True 
    assert is_stable(state_full_board, player, 0, 3) == True 
    assert is_stable(state_full_board, player, 0, 4) == True
    assert is_stable(state_full_board, player, 0, 5) == True 
    assert is_stable(state_full_board, player, 0, 6) == True 
    
    assert is_stable(state_full_board, player, 1, 0) == True 
    assert is_stable(state_full_board, player, 2, 0) == True 
    assert is_stable(state_full_board, player, 3, 0) == True 
    assert is_stable(state_full_board, player, 4, 0) == True
    assert is_stable(state_full_board, player, 5, 0) == True 
    assert is_stable(state_full_board, player, 6, 0) == True
    
    assert is_stable(state_full_board, player, 7, 1) == True 
    assert is_stable(state_full_board, player, 7, 2) == True 
    assert is_stable(state_full_board, player, 7, 3) == True 
    assert is_stable(state_full_board, player, 7, 4) == False
    assert is_stable(state_full_board, player, 7, 5) == False
    assert is_stable(state_full_board, player, 7, 6) == False
    
    assert is_stable(state_full_board, player, 1, 7) == True
    assert is_stable(state_full_board, player, 2, 7) == True
    assert is_stable(state_full_board, player, 3, 7) == True
    assert is_stable(state_full_board, player, 4, 7) == False
    assert is_stable(state_full_board, player, 5, 7) == False
    assert is_stable(state_full_board, player, 6, 7) == False
    
    #initial board
    assert is_stable(state_initial_board, player, 0, 1) == False 
    assert is_stable(state_initial_board, player, 0, 2) == False 
    assert is_stable(state_initial_board, player, 0, 3) == False 
    assert is_stable(state_initial_board, player, 0, 4) == False
    assert is_stable(state_initial_board, player, 0, 5) == False 
    assert is_stable(state_initial_board, player, 0, 6) == False 
    
    assert is_stable(state_initial_board, player, 1, 0) == False 
    assert is_stable(state_initial_board, player, 2, 0) == False 
    assert is_stable(state_initial_board, player, 3, 0) == False 
    assert is_stable(state_initial_board, player, 4, 0) == False
    assert is_stable(state_initial_board, player, 5, 0) == False 
    assert is_stable(state_initial_board, player, 6, 0) == False
    
    assert is_stable(state_initial_board, player, 7, 1) == False 
    assert is_stable(state_initial_board, player, 7, 2) == False 
    assert is_stable(state_initial_board, player, 7, 3) == False 
    assert is_stable(state_initial_board, player, 7, 4) == False
    assert is_stable(state_initial_board, player, 7, 5) == False
    assert is_stable(state_initial_board, player, 7, 6) == False
    
    assert is_stable(state_initial_board, player, 1, 7) == False
    assert is_stable(state_initial_board, player, 2, 7) == False
    assert is_stable(state_initial_board, player, 3, 7) == False
    assert is_stable(state_initial_board, player, 4, 7) == False
    assert is_stable(state_initial_board, player, 5, 7) == False
    assert is_stable(state_initial_board, player, 6, 7) == False

#test that the function return false when the piece is not in corner or boundaries
def test_is_stable_piece_not_corner_boundaries():
    
    player = 'black'
    
    assert is_stable(state_full_board, player, 1, 1) == False
    assert is_stable(state_full_board, player, 3, 4) == False
    
    assert is_stable(state_initial_board, player, 1, 1) == False
    assert is_stable(state_initial_board, player, 3, 4) == False
    
    assert is_stable(state_random_board, player, 1, 1) == False
    assert is_stable(state_random_board, player, 3, 6) == False
         
    
    
#test the stability function when black is the max player
def test_stability_black():
    
    max_player_color = 'black'
    min_player_color = 'white'
    
    expected_result_initial_board = [-2, -2]
    expected_result_full_board = [-6, -2]
    expected_result_random_board = [-8, 1]
    
    assert stability(state_initial_board, max_player_color, min_player_color) == expected_result_initial_board
    assert stability(state_full_board, max_player_color, min_player_color) == expected_result_full_board
    assert stability(state_random_board, max_player_color, min_player_color) == expected_result_random_board

#test the stability function when white is the max player
def test_stability_white():
    
    max_player_color = 'white'
    min_player_color = 'black'
    
    expected_result_initial_board = [-2, -2]
    expected_result_full_board = [-2, -6]
    expected_result_random_board = [1, -8]
    
    assert stability(state_initial_board, max_player_color, min_player_color) == expected_result_initial_board
    assert stability(state_full_board, max_player_color, min_player_color) == expected_result_full_board
    assert stability(state_random_board, max_player_color, min_player_color) == expected_result_random_board
    
#test the controlled_central_squares function when black is the max player
def test_controlled_central_squares_black():
    
    max_player_color = 'black'
    min_player_color = 'white'
    
    expected_result_initial_board = [2, 2]
    expected_result_full_board = [8, 1]
    expected_result_random_board = [5, 1]
    
    assert controlled_central_squares(state_initial_board, max_player_color, min_player_color) == expected_result_initial_board
    assert controlled_central_squares(state_full_board, max_player_color, min_player_color) == expected_result_full_board
    assert controlled_central_squares(state_random_board, max_player_color, min_player_color) == expected_result_random_board
    
#test the controlled_central_squares function when black is the max player
def test_controlled_central_squares_white():
    
    max_player_color = 'white'
    min_player_color = 'black'
    
    expected_result_initial_board = [2, 2]
    expected_result_full_board = [1, 8]
    expected_result_random_board = [1, 5]
    
    assert controlled_central_squares(state_initial_board, max_player_color, min_player_color) == expected_result_initial_board
    assert controlled_central_squares(state_full_board, max_player_color, min_player_color) == expected_result_full_board
    assert controlled_central_squares(state_random_board, max_player_color, min_player_color) == expected_result_random_board
    
    
   
    

    
    
    


