from src.GUI.components.grid import Grid
from src.Game.game_utils_fonction import get_available_moves

class OthelloGame:

    def __init__(self, canvas):
        """initialize the game"""
        
        self.current_player_color = None
        self.max_player_color = None
        self.min_player_color = None
        self.number_circle_max_player = 2
        self.number_circle_min_player = 2
        self.difficulty = None
        self.grid = Grid(canvas)
        self.grid.canvas.bind('<Button-1>', self.on_canvas_click)
        self.initialize_game() 
        self.grid.display_available_moves(get_available_moves(self.grid.state, self.current_player_color), self.current_player_color) #display available moves for the current player
        
    def initialize_game(self):
        """config the initial state of the game and draw the initial pieces on the grid"""
        
        mid = len(self.grid.state) // 2
        self.grid.state[mid-1][mid-1] = "white"
        self.grid.state[mid-1][mid] = "black"
        self.grid.state[mid][mid-1] = "black"
        self.grid.state[mid][mid] = "white"

        # draw on the canva
        self.grid.place_piece(mid-1, mid-1, "white")
        self.grid.place_piece(mid-1, mid, "black")
        self.grid.place_piece(mid, mid-1, "black")
        self.grid.place_piece(mid, mid, "white")
           
    def make_move(self, row, col):
        """Make a move"""
        pass
       
    def flip_circles(self, row, col):
        """change the color of captured circles"""
        pass
    
    def is_valid_move(self, row, col):
        """check if the move is valid"""
        return True
    
    def on_canvas_click(self, event):
        """manages the click event by placing a counter of the player's color in the clicked cel"""
        
        x, y = event.x, event.y
        row, col = self.grid.pixel_to_cell(x, y)
        if row < 8 and col < 8 and self.grid.state[row][col] is None:
            if self.is_valid_move(row, col):
                self.grid.place_piece(row, col, self.current_player_color)  
                self.toggle_player()  # change the player for the next turn
            else:
                print("invalid mouv:",row,col)
                
    def update_number_circle(self):
        """update the number of circle for each player"""
        
        for row in self.grid.state:
            for cell in row:
                if cell == "black":
                    self.number_circle_first_player += 1
                elif cell == "white":
                    self.number_circle_second_player += 1
        self.grid.update_circle_counter(self.number_circle_first_player, self.number_circle_second_player)
        
        
    def toggle_player(self):
        """change the color of the current player"""
        
        self.current_player_color = 'white' if self.current_player_color == 'black' else 'black'
        
    def set_max_player_color(self, color):
        """set the color for the max player(humain player) and the min player(AI)"""
        
        self.max_player_color = color
        self.min_player_color = "white" if color == "black" else "black"
        self.current_player_color = color
        
    
    
        
        
    
            
                
    
        
            
        
        
        
