from src.GUI.components.grid import Grid
from src.Game.game_utils_fonction import get_available_moves, is_valid_move

class OthelloGame:
    
    """ Class representing the logic of the Othello game ^^"""
    

    def __init__(self, canvas):
        """initialize the game"""
        
        self.current_player_color = None
        self.max_player_color = None
        self.min_player_color = None
        self.number_circle_max_player = 2
        self.number_circle_min_player = 2
        self.difficulty = None
        self.available_moves = []
        self.grid = Grid(canvas)
        self.grid.canvas.bind('<Button-1>', self.on_canvas_click)
        self.initialize_game() 
        
    def initialize_game(self):
        """configure the initial state of the game and draw the initial pieces on the grid"""
        
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
        """Make a move

        Args:
            row: The row index of the move.
            col: The column index of the move.
        """
        
        if is_valid_move(self.grid.state,self.current_player_color,row,col):
            self.grid.place_piece(row,col,self.current_player_color) 
            self.flip_circles(row,col) # flip the captured piece
            self.update_number_circle(1, 0) #increment the number of circle by 1 for the current player 
            self.toggle_player()
        else:
            print("invalid move at : ",row,col)
            
    def is_valid_move(self, row, col):
        """Check if the move is valid in any direction."""
        
        return (row, col) in self.available_moves
    
       
    def flip_circles(self, row, col):
        """Change the color of captured circles (flip)

        Args:
            row: The row index of the move.
            col: The column index of the move.
        """
        player_color = self.current_player_color
        opponent_color = self.min_player_color if player_color == self.max_player_color else self.max_player_color
        
        board_size = len(self.grid.state)
        
        # check all directions
        for d_row, d_col in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
            cur_row, cur_col = row + d_row, col + d_col
            found_opponent = False
            to_flip = []

            # check if the bounds of the grid and the cell at (cur_row, cur_col) contains the opponent's color
            while cur_row in range(board_size) and cur_col in range(board_size) and self.grid.state[cur_row][cur_col] == opponent_color:
                to_flip.append((cur_row, cur_col))
                cur_row += d_row
                cur_col += d_col
                found_opponent = True

            # if piece found and followed by the current player's piece => the move is valid and flip the pieces
            if found_opponent and cur_row in range(board_size) and cur_col in range(board_size) and self.grid.state[cur_row][cur_col] == player_color:
                for flip_row, flip_col in to_flip:
                    self.grid.place_piece(flip_row, flip_col, player_color)
                    self.grid.state[flip_row][flip_col] = player_color #update the state of the grid
                    self.update_number_circle(0, 1) 
        
    
    def on_canvas_click(self, event):
        """manages the click event by placing a counter of the player's color in the clicked cel"""
        
        x, y = event.x, event.y
        row, col = self.grid.pixel_to_cell(x, y)
        if row < 8 and col < 8 and self.grid.state[row][col] is None:
            if self.is_valid_move(row, col):
                self.grid.place_piece(row, col, self.current_player_color)
                self.grid.state[row][col] = self.current_player_color #update the state of the grid
                self.update_number_circle(1, 0) #increment the number of circle by 1 for the current player
                self.flip_circles(row, col)  # flip the captured piece
                self.game_loop(False)
               
            else:
                print("invalid move at :",row,col)
                
    def update_number_circle(self, new_circle, fliped_circles):
        """update the number of circle for each player"""
        
        self.number_circle_max_player = self.number_circle_max_player + new_circle + fliped_circles if self.max_player_color == self.current_player_color else self.number_circle_max_player - fliped_circles
        self.number_circle_min_player = self.number_circle_min_player + new_circle + fliped_circles if self.min_player_color == self.current_player_color else self.number_circle_min_player - fliped_circles
        
                    
        white_circles, black_circles = (self.number_circle_max_player, self.number_circle_min_player) if self.max_player_color == 'black' else (self.min_player_color, self.max_player_color)            
        self.grid.update_circle_counter(white_circles, black_circles)
                
    def toggle_player(self):
        """change the color of the current player"""
        
        self.current_player_color = 'white' if self.current_player_color == 'black' else 'black'
        
    def set_max_player_color(self, color):
        """set the color for the max player(humain player) and the min player(AI)"""
        
        self.max_player_color = color
        self.min_player_color = "white" if color == "black" else "black"
        self.current_player_color = color
        
    
    def is_game_over(self):
        """check if the game is over"""
        if len(self.available_moves) == 0:
            # aucun coup possible pour le joueur actuel
            return True
        return False

    def determine_winner(self):
        """determine the winner of the game"""
        black_count = sum(row.count("black") for row in self.grid.state)
        white_count = sum(row.count("white") for row in self.grid.state)

        if black_count > white_count:
            return "Le joueur NOIR a gagné !"
        elif black_count < white_count:
            return "Le joueur BLANC a gagné !"
        else:
            return "It's a draw !"
        
    def game_loop(self, first_call):
        """run the game"""
        
        if(not first_call):
            self.toggle_player()  # change the player for the next turn  
            
        self.grid.resset_available_moves(self.available_moves) #avoid having the available moves from the previous turn
        self.available_moves = get_available_moves(self.grid.state, self.current_player_color)
        self.grid.display_available_moves(self.available_moves, self.current_player_color)
    
        if(self.is_game_over()):
            print(self.determine_winner())
            return            
        
        
            

            
            
        
    
            
                
    
        
            
        
        
        
