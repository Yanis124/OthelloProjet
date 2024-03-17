import sys
import os
current_dir = os.getcwd()

# Navigate to the parent directory
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../'))
sys.path.append(src_path)
print(src_path)

from src.Game.game_utils_fonction import get_available_moves, is_valid_move
from src.GUI.constantes import CANVAS_WIDTH, CANVAS_HEIGHT

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(src_path)
print(src_path)
from src.ai.heuristics.test_config import *

def test_get_available_moves_black():
    """test the get available moves function when black is the current player"""
    
    current_player_color = "black"
    available_moves_initial_board = [(2, 3), (3, 2), (4, 5), (5, 4)]
    available_moves_full_board = []
    available_moves_random_board = [(0, 3), (1, 0), (1, 5), (1, 7), (2, 3), (3, 3), (4, 2), (4, 6), (5, 7), (7, 4)]
    
    assert get_available_moves(state_initial_board, current_player_color) == available_moves_initial_board
    assert get_available_moves(state_full_board, current_player_color) == available_moves_full_board
    assert get_available_moves(state_random_board, current_player_color) == available_moves_random_board 
    
def test_get_available_moves_white():
    """test the get available moves function when white is the current player"""
    
    current_player_color = "white"
    available_moves_initial_board = [(2, 4), (3, 5), (4, 2), (5, 3)]
    available_moves_full_board = []
    available_moves_random_board = [(0, 6), (1, 0), (2, 3), (2, 5), (3, 3), (4, 2), (4, 6), (5, 7), (6,1), (7, 4)]
    
    assert get_available_moves(state_initial_board, current_player_color) == available_moves_initial_board
    assert get_available_moves(state_full_board, current_player_color) == available_moves_full_board        
    assert get_available_moves(state_random_board, current_player_color) == available_moves_random_board
    

    
    