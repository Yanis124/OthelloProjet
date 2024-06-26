import tkinter as tk
from src.GUI.constantes import SQUARE_SIZE,CANVAS_HEIGHT,GRID_COLOR, BORDER_COLOR, CANVAS_WIDTH, TITLE_TEXT_FONT, CIRCLE_RADIUS, NUMBER_CIRCLE_SIZE, BLACK_CIRCLE_X_CORDINATE, WHITE_CIRCLE_X_CORDINATE
from src.GUI.components.circle import Circle

class Grid:
    def __init__(self, canvas):
        """
        initialse the grid, draw the counter of circle for each player

        Args:
            canvas : represente the element where the grid will be drawn
        """
        self.state = [[None for _ in range(8)] for _ in range(8)]  # 8x8 state matrix initialized to None
        if canvas is not None:
            self.canvas = canvas
            self.init_grid()
            self.draw_circle_counter() #draw the two circles that represent the number of circle for each player
            self.init_circle_counter() #draw the number that represent the number of circle for each player
            self.text_id_max_player = None
            self.text_id_min_player = None
            
    def init_grid(self):
        """initialize the grid"""
    
        cell_width = SQUARE_SIZE
        cell_height = SQUARE_SIZE
        for i in range(8):
            for j in range(8):
                x0 = i * cell_width
                y0 = j * cell_height
                x1 = x0 + cell_width
                y1 = y0 + cell_height
                self.canvas.create_rectangle(x0, y0, x1, y1, fill = GRID_COLOR, outline = BORDER_COLOR)

    def draw_circle_counter(self):
        """ draw the circle counter """
                
        circle_radius = CIRCLE_RADIUS
        circle_y = CANVAS_HEIGHT - (2 * CIRCLE_RADIUS + NUMBER_CIRCLE_SIZE)  
        
        self.canvas.create_oval(BLACK_CIRCLE_X_CORDINATE - circle_radius, circle_y - circle_radius,
                           BLACK_CIRCLE_X_CORDINATE + circle_radius, circle_y + circle_radius,
                           fill="black")
        
        self.canvas.create_oval(WHITE_CIRCLE_X_CORDINATE - circle_radius, circle_y - circle_radius,
                           WHITE_CIRCLE_X_CORDINATE + circle_radius, circle_y + circle_radius,
                           fill="white")
        
    def init_circle_counter(self):
        """Initialize the circle counter that represents the number of circles for each player"""
        
        number_y = CANVAS_HEIGHT - (NUMBER_CIRCLE_SIZE + 10)   
        
        self.text_id_max_player = self.canvas.create_text(BLACK_CIRCLE_X_CORDINATE, number_y, text = str(2), font = TITLE_TEXT_FONT)
        self.text_id_min_player = self.canvas.create_text(WHITE_CIRCLE_X_CORDINATE, number_y, text = str(2), font = TITLE_TEXT_FONT)
        
        

    def update_circle_counter(self, number_circle_black_player, number_circle_white_player):
        """Update the circle counters with the current number of circles for each player"""
        
        texts = [item_id for item_id in self.canvas.find_all() if self.canvas.type(item_id) == "text"]

        self.canvas.itemconfigure(texts[0], text = str(number_circle_black_player))
        self.canvas.itemconfigure(texts[1], text = str(number_circle_white_player))
        
    def pixel_to_cell(self, x, y):
        """converts pixels coordinates to grill cell coordinates"""
        
        row = y // SQUARE_SIZE
        col = x // SQUARE_SIZE
        return int(row), int(col)
    
    
    def place_piece(self, row, col, color):
        """place a circle in a specific cell"""
        
        circle = Circle(self.canvas, col, row, color)
        circle.draw_circle()  # draw a circle in the specified cell with the specified color  
        
    def display_available_moves(self, available_moves, currnet_player_color):
        """display the available moves for the current player"""
        
        for move in available_moves:
            circle = Circle(self.canvas, move[1], move[0], currnet_player_color )
            circle.draw_outlined_circle()
            
    def resset_available_moves(self, available_moves):
        """remove the available moves from the grid"""
        
        for move in available_moves:
            circle = Circle(self.canvas, move[1], move[0], GRID_COLOR)
            circle.draw_outlined_circle()
        
        
                

           
            
    

        
        
