import tkinter as tk
from src.GUI.constantes import SQUARE_SIZE,CANVAS_HEIGHT,GRID_COLOR, BORDER_COLOR, CANVAS_WIDTH, TITLE_TEXT_FONT, CIRCLE_RADIUS, NUMBER_CIRCLE_SIZE, BLACK_CIRCLE_X_CORDINATE, WHITE_CIRCLE_X_CORDINATE
from src.GUI.components.circle import Circle

class Grid:
    def __init__(self, canvas, game):
        """
        initialse the grid, draw the counter of circle for each player

        Args:
            canvas : represente the element where the grid will be drawn
        """
      
        self.canvas = canvas
        self.number_circle_first_player = 2
        self.number_circle_second_player = 2
        self.game = game
        self.difficulty = None
        self.first_player_color = None #first player is the humain player
        self.second_player_color = None #second player is the AI 
        self.current_player = None

        self.state = [[None for _ in range(8)] for _ in range(8)]  # 8x8 state matrix initialized to None
        self.init_grid()
        self.initialize_game() 
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

    def initialize_game(self):
        """config the initial state of the game and draw the initial pieces on the grid"""
        
        mid = len(self.state) // 2
        self.state[mid-1][mid-1] = "white"
        self.state[mid-1][mid] = "black"
        self.state[mid][mid-1] = "black"
        self.state[mid][mid] = "white"

        # draw on the canva
        self.place_piece(mid-1, mid-1, "white")
        self.place_piece(mid-1, mid, "black")
        self.place_piece(mid, mid-1, "black")
        self.place_piece(mid, mid, "white")
     

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
        
        self.canvas.create_text(BLACK_CIRCLE_X_CORDINATE, number_y, text = str(2), font = TITLE_TEXT_FONT)
        self.canvas.create_text(WHITE_CIRCLE_X_CORDINATE, number_y, text = str(2), font = TITLE_TEXT_FONT)

    def update_circle_counter(self, number_circle_first_player, number_circle_second_player):
        """Update the circle counters with the current number of circles for each player"""
        
        self.canvas.itemconfigure(self.text_id_first_player, text = str(number_circle_first_player))
        self.canvas.itemconfigure(self.text_id_second_player, text = str(number_circle_second_player))
        
    def update_number_circle(self):
        """update the number of circle for each player"""
        
        for row in self.state:
            for cell in row:
                if cell == "black":
                    self.number_circle_first_player += 1
                elif cell == "white":
                    self.number_circle_second_player += 1
        

    def pixel_to_cell(self, x, y):
        """converts pixels coordinates to grill cell coordinates"""
        
        row = y // SQUARE_SIZE
        col = x // SQUARE_SIZE
        return int(row), int(col)

    def is_valid_move(self, row, col, player_color):
        """check if the move is valid"""
        
        if self.state[row][col] is not None:  # the cell isnt empty
            return False
        
        return True

    def on_canvas_click(self, event):
        """manages the click event by placing a counter of the player's color in the clicked cel"""
        
        x, y = event.x, event.y
        row, col = self.pixel_to_cell(x, y)
        if row < 8 and col < 8 and self.state[row][col] is None:
            if self.is_valid_move(row, col, self.current_player):
                print("valide mouv:", row, col)
                self.place_piece(row, col, self.current_player)  # use the current's player color
                self.toggle_player()  # change the player for the next turn
            else:
                print("invalid mouv:",row,col)
           
            
    def place_piece(self, row, col, color):
        """place a circle in a specific cell"""
        print(color)
        circle = Circle(self.canvas, col, row, color)
        circle.draw_circle()  # draw a circle in the specified cell with the specified color

    def toggle_player(self):
        """change the color of the current player"""
        self.current_player = 'white' if self.current_player == 'black' else 'black'
        
    def set_first_player_color(self, color):
        """Set the color of the first player"""
        
        if color == "Noir":
            self.current_player = self.first_player_color = "black"
            self.second_player_color = "white"
            
        else : 
            self.current_player = self.first_player_color = "white"
            self.second_player_color = "black"
        
        
