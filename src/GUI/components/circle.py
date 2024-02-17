import tkinter as tk
from src.GUI.constantes import CIRCLE_RADIUS, SQUARE_SIZE

class Circle:
    def __init__(self, canvas, row, col, color):
        """
        initialse the circle 

        Args:
            canvas : represente the elemenet where the circle will be drawn
            row : the row where the circle will be drawn
            col : the col where the circle will be drawn
            color : the color of the circle
        """
        self.canvas = canvas
        self.row = row
        self.col = col
        self.color = color
        
    def draw_circle(self):
        """ draw a circle inside the grid """
        
        self.canvas.create_oval(self.row * SQUARE_SIZE + 5, self.col * SQUARE_SIZE + 5 ,
                           (self.row * SQUARE_SIZE) + CIRCLE_RADIUS * 2 - 5, (self.col * SQUARE_SIZE) + CIRCLE_RADIUS * 2 - 5,
                           fill = self.color)
        
    def draw_outlined_circle(self):
        """ draw a circle inside the grid with an outline """
        
        self.canvas.create_oval(self.row * SQUARE_SIZE + 5, self.col * SQUARE_SIZE + 5 ,
                           (self.row * SQUARE_SIZE) + CIRCLE_RADIUS * 2 - 5, (self.col * SQUARE_SIZE) + CIRCLE_RADIUS * 2 - 5,
                            outline = "white")
        
        
        