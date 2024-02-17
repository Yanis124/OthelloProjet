import tkinter as tk
from src.GUI.constantes import BUTTON_STYLE, PAGE_BG_COLOR, TITLE_TEXT_FONT, BORDER_COLOR, GRID_COLOR, CANVAS_WIDTH, CANVAS_HEIGHT, CIRCLE_RADIUS, NUMBER_CIRCLE_SIZE, BLACK_CIRCLE_X_CORDINATE, WHITE_CIRCLE_X_CORDINATE
from src.GUI.components.grid import Grid

class GamePage(tk.Frame):
    def __init__(self, parent, controller, HomePage):
        """Initialize GamePage

        Args:
            parent : the layout that containe this page
            controller : unable GamePage to interacte with the main app (passe information, change page, etc.)
        """
        tk.Frame.__init__(self, parent, bg = PAGE_BG_COLOR)  

        self.difficulty_text = "Easy"
        
        #add a label
        self.label = tk.Label(self, text = "Difficulty: " + self.difficulty_text, font = TITLE_TEXT_FONT, bg = '#2c3e50', fg = 'white')
        self.label.grid(row= 0, column = 0, pady = 10, padx = 10, sticky = 'ew')

        #add a button to go back to the MenuPage
        button = tk.Button(self, text = "Go Back to the Menu", command = lambda: controller.show_frame(HomePage), **BUTTON_STYLE)
        button.grid(row = 1, column = 0, pady = 10, padx = 10, sticky = 'ew')

        # add the canvas that will contain the grid
        self.canvas = tk.Canvas(self, bg = PAGE_BG_COLOR, highlightthickness = 0)
        self.canvas.grid(row = 2, column = 0, pady = (10,10), sticky = 'nsew')

        self.grid_game = Grid(self.canvas)  # the name grid is already taken by the grid layout

        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def set_difficulty(self, difficulty):
        """Change the difficulty of the game"""
        
        self.difficulty_text = difficulty.capitalize()
        self.label.config(text = "Difficulty: " + self.difficulty_text)




        
        
        
        
                        
   