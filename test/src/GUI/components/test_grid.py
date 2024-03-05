import pytest
import sys
import os
current_dir = os.getcwd()

# Navigate to the parent directory
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../'))
sys.path.append(src_path)

from tkinter import Tk, Canvas
from src.GUI.components.grid import Grid  
from src.GUI.constantes import CANVAS_WIDTH, CANVAS_HEIGHT

@pytest.fixture
def canvas():
    """create a new canvas for each test"""
    root = Tk()
    canvas = Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    yield canvas
    root.destroy()

def test_init_grid_dimension(canvas):
    """test the init grid function that initialize the grid in the canvas"""
    grid = Grid(canvas)
    assert len(grid.state) == 8
    assert len(grid.state[0]) == 8
    

def test_draw_circle_counter(canvas):
    """test the draw circle counter function that draw the circle counter for each player"""
    
    grid = Grid(canvas)
    circles = [item_id for item_id in grid.canvas.find_all() if canvas.type(item_id) == "oval"]
    assert len(circles) == 2  # Two circles for each player


def test_place_piece(canvas):
    """test the place piece function that place a piece in the grid and draw the circle in the canvas"""
    
    grid = Grid(canvas)
    grid.place_piece(0, 0, "black")
    grid.place_piece(1, 1, "white")
    circles = [item_id for item_id in grid.canvas.find_all() if canvas.type(item_id) == "oval"]
    assert len(circles) == 4  # Two circles should be drawn + 2 circle that represent the number of circle for each player
    
def test_pixel_to_cell(canvas):
    """test the pixel to cell function that convert the pixel coordinate to the cell coordinate in the grid"""
    
    grid = Grid(canvas)
    assert grid.pixel_to_cell(0, 0) == (0, 0)
    assert grid.pixel_to_cell(100, 100) == (1, 1)
    assert grid.pixel_to_cell(160, 120) == (1, 2)
    
    
# def test_toggle_player_black(canvas):
#     """test the toggle player function that change the current player from black to white"""
    
#     grid = Grid(canvas)
#     grid.current_player = "black"
#     grid.toggle_player()
#     assert grid.current_player == "white"
    
# def test_toggle_player_white(canvas):
#     """test the toggle player function that change the current player from white to black"""
    
#     grid = Grid(canvas)
#     grid.current_player = "white"
#     grid.toggle_player()
#     assert grid.current_player == "black"
    
    

