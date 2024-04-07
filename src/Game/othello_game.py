from src.GUI.components.grid import Grid
from src.Game.game_utils_fonction import get_available_moves, is_valid_move, get_flip_circles, is_game_over
from src.ai.ai.minimax import get_best_move
from src.ai.heuristics.easy_ai_eval import easy_ai_utility
from src.ai.heuristics.normal_ai_eval import normal_ai_utility
from src.ai.heuristics.hard_ai_eval import hard_ai_utility

import time
from tkinter import Tk

class OthelloGame:
    """ Class representing the logic of the Othello game ^^"""
    
    #AI constants
    EASY_AI = (2, easy_ai_utility)
    NORMAL_AI = (0, normal_ai_utility)
    HARD_AI = (5, hard_ai_utility)
    
    LIST_DIFFICULTY = [EASY_AI, NORMAL_AI, HARD_AI]

    def __init__(self, canvas):
        """initialize the game"""
        
        self.current_player_color = None
        self.max_player_color = None
        self.min_player_color = None
        self.number_circle_max_player = 2
        self.number_circle_min_player = 2
        self.difficulty = None
        self.game_mode = None
        self.max_ai_parametres = (None, None)
        self.min_ai_parametres = (None, None) 
        self.available_moves = [] 
        self.delay = 1000 
        
        if canvas is not None:
            self.canvas = canvas
            self.grid = Grid(canvas)
            self.grid.canvas.bind('<Button-1>', self.on_canvas_click)
        else:
            self.canvas = None
            self.grid = Grid(None)
            
        self.initialize_game() 
        
    def initialize_game(self):
        """configure the initial state of the game and draw the initial pieces on the grid"""
        
        mid = len(self.grid.state) // 2
        self.grid.state[mid-1][mid-1] = "white"
        self.grid.state[mid-1][mid] = "black"
        self.grid.state[mid][mid-1] = "black"
        self.grid.state[mid][mid] = "white"

        # draw on the canva
        if self.canvas is not None:
            self.grid.place_piece(mid-1, mid-1, "white")
            self.grid.place_piece(mid-1, mid, "black")
            self.grid.place_piece(mid, mid-1, "black")
            self.grid.place_piece(mid, mid, "white")
           
    def make_move(self, row = None, col = None):
        """Make a move

        Args:
            row: The row index of the move.
            col: The column index of the move.
        """
            
        if is_valid_move(self.grid.state, self.current_player_color, row, col):
            
            if row is not None or col is not None:
                if self.canvas is not None:
                    self.grid.place_piece(row, col, self.current_player_color)
                self.grid.state[row][col] = self.current_player_color #update the state of the grid
                print(f"{self.current_player_color.capitalize()} joue en {row}, {col}")
                self.update_number_circle(1, 0) #increment the number of circle by 1 for the current player
                self.flip_circles(row, col)  # flip the captured piece
               
            self.game_loop(False)
            
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
        
        list_flipped_circles = get_flip_circles(self.grid.state,self.current_player_color, row, col)
        
        for flip_circle in list_flipped_circles:
            flip_row, flip_col = flip_circle[0], flip_circle[1]
            self.grid.state[flip_row][flip_col] = self.current_player_color
            
            if self.canvas is not None:
                self.grid.place_piece(flip_row, flip_col, self.current_player_color)
         
        self.update_number_circle(0, len(list_flipped_circles)) 
    
    def on_canvas_click(self, event):
        """manages the click event by placing a counter of the player's color in the clicked cel"""
        
        x, y = event.x, event.y
        row, col = self.grid.pixel_to_cell(x, y)

        if row < 8 and col < 8 and self.grid.state[row][col] is None:
           self.make_move(row, col)
                
    def update_number_circle(self, new_circle, fliped_circles):
        """update the number of circle for each player"""
        
        self.number_circle_max_player = self.number_circle_max_player + new_circle + fliped_circles if self.max_player_color == self.current_player_color else self.number_circle_max_player - fliped_circles
        self.number_circle_min_player = self.number_circle_min_player + new_circle + fliped_circles if self.min_player_color == self.current_player_color else self.number_circle_min_player - fliped_circles
             
        white_circles, black_circles = (self.number_circle_max_player, self.number_circle_min_player) if self.max_player_color == 'black' else (self.number_circle_min_player ,self.number_circle_max_player)  
        
        if self.canvas is not None:          
            self.grid.update_circle_counter(white_circles, black_circles)
                
    def toggle_player(self):
        """change the color of the current player"""
        
        self.current_player_color = 'white' if self.current_player_color == 'black' else 'black'
        
    def set_max_player_color(self, color):
        """set the color for the max player and the min player"""
        
        self.min_player_color = color
        self.max_player_color = "white" if color == "black" else "black"
        self.current_player_color = color
        
    def determine_winner(self):
        """determine the winner of the game adn return the number of circle for each player"""
        
        max_player_count = sum(row.count(self.max_player_color) for row in self.grid.state)
        min_player_count = sum(row.count(self.min_player_color) for row in self.grid.state)

        if max_player_count > min_player_count:
            print("Le joueur Max a gagné !")
        elif max_player_count < min_player_count:
            print("Le joueur Min a gagné !")
        else:
            print("It's a draw !")
        
    def set_ai_parametres(self):
        """Set the depth and evaluation function of the minimax algorithm"""
        
        self.max_ai_parametres = self.HARD_AI  if self.difficulty == "Hard" else (self.NORMAL_AI if self.difficulty == "Normal" else self.EASY_AI)
        
    def game_loop(self, first_call):
        """run the game"""
                
        print("\n------------------------------------------------")

        if not first_call :
            self.toggle_player()  # change the player for the next turn 
            
        if self.game_mode == "ai_vs_ai":
            self.available_moves = get_available_moves(self.grid.state, self.current_player_color)
        else :
            self.grid.resset_available_moves(self.available_moves) #avoid having the available moves from the previous turn
            self.available_moves = get_available_moves(self.grid.state, self.current_player_color)
            self.grid.display_available_moves(self.available_moves, self.current_player_color)  
            
        if is_game_over(self.available_moves):
            self.determine_winner()
            return 
        
        if self.current_player_color == self.max_player_color and self.game_mode == "player_vs_ai": #ai vs player (ai is the max player player is the min player)
            self.play_best_move(self.max_ai_parametres[0], self.max_ai_parametres[1])
        elif self.current_player_color == self.min_player_color and self.game_mode == "ai_vs_ai": #ai vs ai (first ai is the max player and the second ai is the min player)
            self.play_best_move(self.min_ai_parametres[0], self.min_ai_parametres[1])
            
    def play_best_move(self, depth, utility_function):
        """play the best move for the AI"""
        
        ai_move = get_best_move(self.grid.state, min_player_color = self.min_player_color, max_player_color = self.max_player_color, current_player_color = self.current_player_color, depth = depth,  utility_function = utility_function)
        print(ai_move)
        if ai_move is None:
            self.game_loop(False)
            return
        self.make_move(ai_move[0], ai_move[1])
     
    def ai_vs_ai(self, max_ai_difficulty, min_ai_difficulty):
        """run a game between two ai"""
        
        self.game_mode = "ai_vs_ai"
        self.max_player_color = "white"
        self.min_player_color = "black"
        self.current_player_color = "white"
        self.max_ai_parametres = self.LIST_DIFFICULTY[max_ai_difficulty]
        self.min_ai_parametres = self.LIST_DIFFICULTY[min_ai_difficulty]        
        self.game_loop(True)
        return (self.number_circle_max_player, self.number_circle_min_player)
        
        
    
                    
        
        
            

            
            
        
    
            
                
    
        
            
        
        
        
