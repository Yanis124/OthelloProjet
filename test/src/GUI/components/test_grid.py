import pytest
import sys
import os
current_dir = os.getcwd()

# Navigate to the parent directory
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../'))
sys.path.append(src_path)

from tkinter import Tk, Canvas
from src.GUI.components.grid import Grid  
from src.GUI.constantes import CANVAS_WIDTH, CANVAS_HEIGHT, SQUARE_SIZE

@pytest.fixture
def canvas():
    """create a new canvas for each test"""
    root = Tk()
    canvas = Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    yield canvas
    root.destroy()

#test the init grid function that initialize the grid in the canvas
def test_init_grid_dimension(canvas):

    grid = Grid(canvas)
    assert len(grid.state) == 8
    assert len(grid.state[0]) == 8
    
#test the draw circle counter function that draw the circle counter for each player
def test_draw_circle_counter(canvas):
    
    grid = Grid(canvas)
    circles = [item_id for item_id in grid.canvas.find_all() if canvas.type(item_id) == "oval"]
    assert len(circles) == 2  # Two circles for each player


#test update circle counter function that update the number of circle for each player
def test_update_circle_counter(canvas):
    
    grid = Grid(canvas)
    number_circles_black_player = 10
    number_circles_white_player = 15
    grid.update_circle_counter(number_circles_black_player, number_circles_white_player)
    texts = [item_id for item_id in grid.canvas.find_all() if grid.canvas.type(item_id) == "text"]
    assert len(texts) == 2 
    
    assert grid.canvas.itemcget(texts[0], "text") == str(number_circles_black_player)
    assert grid.canvas.itemcget(texts[1], "text") == str(number_circles_white_player)
    

#test the place piece function that place a piece in the grid and draw the circle in the canvas
def test_place_piece(canvas):
    
    grid = Grid(canvas)
    grid.place_piece(0, 0, "black")
    grid.place_piece(1, 1, "white")
    circles = [item_id for item_id in grid.canvas.find_all() if canvas.type(item_id) == "oval"]
    assert len(circles) == 4  # Two circles should be drawn + 2 circle that represent the number of circle for each player
    
#test the pixel to cell function that convert the pixel coordinate to the cell coordinate in the grid
def test_pixel_to_cell(canvas):
    
    grid = Grid(canvas)
    assert grid.pixel_to_cell(0, 0) == (0, 0)
    assert grid.pixel_to_cell(100, 100) == (1, 1)
    assert grid.pixel_to_cell(160, 120) == (1, 2)
    
    
    

    
    
    

