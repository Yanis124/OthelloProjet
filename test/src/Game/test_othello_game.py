import pytest
import sys
import os
current_dir = os.getcwd()

# Navigate to the parent directory
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../'))
sys.path.append(src_path)

from tkinter import Tk, Canvas
from src.Game.othello_game import OthelloGame
from src.Game.game_utils_fonction import is_game_over
from src.GUI.constantes import CANVAS_WIDTH, CANVAS_HEIGHT

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(src_path)
print(src_path)
from src.ai.heuristics.test_config import *

@pytest.fixture
def canvas():
    """create a new canvas for each test"""
    root = Tk()
    canvas = Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    yield canvas
    root.destroy()

def test_initialize_game(canvas):
    """test the initialize game function that set the initial state of the game"""
    
    game =OthelloGame(canvas)

    assert game.grid.state[3][3] == "white"
    assert game.grid.state[3][4] == "black"
    assert game.grid.state[4][3] == "black"
    assert game.grid.state[4][4] == "white"
    
def test_flip_circles_black(canvas):
    """test the flip circle function when black is the current player"""
    
    current_player = "black"
    game = OthelloGame(canvas)
    game.set_min_player_color(current_player)
    
    #initial state of the grid
    move_initial_board = (2, 3)
    fliped_circles = [(3, 3)]
    game.make_move(move_initial_board[0], move_initial_board[1])
    
    for fliped_circles in fliped_circles:
        assert game.grid.state[fliped_circles[0]][fliped_circles[1]] == current_player
        
    #random state of the grid
    game.grid.state = state_random_board
    game.toggle_player() #reset the player to black
    move_random_board = (0, 3)
    fliped_circles = [(0, 2), (0, 4), (1, 2), (2, 1)]
    game.make_move(move_random_board[0], move_random_board[1])
    
    for fliped_circles in fliped_circles:
        assert game.grid.state[fliped_circles[0]][fliped_circles[1]] == current_player
    
def test_update_number_circle_black(canvas):
    """test the update number function that update the number of circles for each player when the current player is black"""
    
    game = OthelloGame(canvas)
    game.current_player_color = "black"
    game.max_player_color = "black"
    game.min_player_color = "white"
    fliped_circles = 1
    expected_number_circle_max_player = 4
    expected_number_circle_min_player = 1
    game.update_number_circle(1, fliped_circles)
    
    assert game.number_circle_max_player == expected_number_circle_max_player
    assert game.number_circle_min_player == expected_number_circle_min_player  
    
def test_update_number_circle_white(canvas):
    """test the update number function that update the number of circles for each player when the current player is black"""
    
    game = OthelloGame(canvas)
    game.current_player_color = "white"
    game.max_player_color = "white"
    game.min_player_color = "black"
    fliped_circles = 1
    expected_number_circle_max_player = 4
    expected_number_circle_min_player = 1
    game.update_number_circle(1, fliped_circles)
    
    assert game.number_circle_max_player == expected_number_circle_max_player
    assert game.number_circle_min_player == expected_number_circle_min_player  
    
def test_set_min_player_color_black(canvas):
    """test the set max player function that it set the max player and current player to the one passed on parametre"""
    
    max_player_color = "black"
    min_player_color = "white"
    game = OthelloGame(canvas)
    game.set_min_player_color(min_player_color)
    
    assert game.max_player_color == max_player_color
    assert game.min_player_color == min_player_color
    assert game.current_player_color == min_player_color 
    
def test_set_min_player_color_white(canvas):
    """test the set max player function that it set the max player and current player to the one passed on parametre"""
    
    max_player_color = "white"
    min_player_color = "black"
    game = OthelloGame(canvas)
    game.set_min_player_color(min_player_color)
    
    assert game.max_player_color == max_player_color
    assert game.min_player_color == min_player_color
    assert game.current_player_color == min_player_color 
    
def test_toggle_player_black(canvas):
    """test the toggle player function that change the current player from black to white"""
    
    game = OthelloGame(canvas)
    game.current_player_color = "black"
    game.toggle_player()
    assert game.current_player_color == "white"
    
def test_toggle_player_white(canvas):
    """test the toggle player function that change the current player from black to white"""
    
    game =OthelloGame(canvas)
    game.current_player_color = "white"
    game.toggle_player()
    assert game.current_player_color == "black"
    
def test_is_game_over(canvas):
    """test the is game over function that return True if there is no valide moves left"""
    
    game =OthelloGame(canvas)
    game.grid.state = state_initial_board
    game.game_loop(True)
    assert is_game_over(game.available_moves) == False
    
    game.grid.state = state_full_board
    game.game_loop(True)
    assert is_game_over(game.available_moves) == True
    
    
