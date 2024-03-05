import pytest
import sys
import os
current_dir = os.getcwd()

# Navigate to the parent directory
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../'))
sys.path.append(src_path)

from tkinter import Tk, Canvas
from src.Game.othello_game import OthelloGame
from src.GUI.constantes import CANVAS_WIDTH, CANVAS_HEIGHT

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
    game.initialize_game()
    assert game.grid.state[3][3] == "white"
    assert game.grid.state[3][4] == "black"
    assert game.grid.state[4][3] == "black"
    assert game.grid.state[4][4] == "white"


def test_toggle_player_black(canvas):
    """test the toggle player function that change the current player from black to white"""
    
    game =OthelloGame(canvas)
    game.current_player_color = "black"
    game.toggle_player()
    assert game.current_player_color == "white"
    
def test_toggle_player_black(canvas):
    """test the toggle player function that change the current player from black to white"""
    
    game =OthelloGame(canvas)
    game.current_player_color = "white"
    game.toggle_player()
    assert game.current_player_color == "black"

def test_set_max_player_color_black(canvas):
    """test the set max player color function that set the max player color to black and the min player color to white"""
    
    game =OthelloGame(canvas)
    game.set_max_player_color("black")
    assert game.max_player_color == "black"
    assert game.min_player_color == "white"
    assert game.current_player_color == "black"
    
def test_set_max_player_color_white(canvas):
    """test the set max player color function that set the max player color to white and the min player color to black"""
    
    game =OthelloGame(canvas)
    game.set_max_player_color("white")
    assert game.max_player_color == "white"
    assert game.min_player_color == "black"
    assert game.current_player_color == "white"