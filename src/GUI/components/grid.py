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
        self.canvas = canvas
        self.text_id_first_player = None
        self.text_id_second_player = None

        self.current_player = None
        
        self.init_grid()
        self.draw_circle_counter() #draw the two circles that represent the number of circle for each player
        self.init_circle_counter() #draw the number that represent the number of circle for each player
  
        self.canvas.bind('<Button-1>', self.on_canvas_click)

     
        
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
        
        self.text_id_first_player = self.canvas.create_text(BLACK_CIRCLE_X_CORDINATE, number_y, text = str(2), font = TITLE_TEXT_FONT)
        self.text_id_second_player = self.canvas.create_text(WHITE_CIRCLE_X_CORDINATE, number_y, text = str(2), font = TITLE_TEXT_FONT)

    def update_circle_counter(self, number_circle_first_player, number_circle_second_player):
        """Update the circle counters with the current number of circles for each player"""
        
        self.canvas.itemconfigure(self.text_id_first_player, text = str(number_circle_first_player))
        self.canvas.itemconfigure(self.text_id_second_player, text = str(number_circle_second_player))
        

    def pixel_to_cell(self, x, y):
        """converts pixels coordinates to grill cell coordinates"""
        row = y // SQUARE_SIZE
        col = x // SQUARE_SIZE
        return row, col

    def on_canvas_click(self, event):
            """manages the click event by placing a counter of the player's color in the clicked cel"""
            x, y = event.x, event.y
            row, col = self.pixel_to_cell(x, y)
            if row < 8 and col < 8:
                print("Clicked cell:", row, col)
                self.place_piece(row, col, self.current_player)  # use the current's player color
                self.toggle_player()  # change the player for the next turn


    def place_piece(self, row, col, color):
        """Place un pion de la couleur spécifiée dans la cellule spécifiée"""
        circle = Circle(self.canvas, col, row, color)
        circle.draw_circle()  # draw a circle in the specified cell with the specified color

    def toggle_player(self):
        """Change le joueur actuel pour le prochain tour"""
        self.current_player = 'white' if self.current_player == 'black' else 'black'
        
