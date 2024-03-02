class OthelloGame:

    def __init__(self):
        self.current_player = 1  # Joueur 1 commence

    def switch_player(self):
        self.current_player *= -1  
   
    def is_valid_move(self, row, col):
        """check if the move is valid"""
        return True

    def make_move(self, row, col):
        """Make a move"""
        pass
       
    def flip_disks(self, row, col):
        """change the color of captured circles"""
        pass
    
    def set_difficulty_game(self, difficulty):
        """Set the difficulty of the game"""
        self.difficulty_game = difficulty

            
                
    
        
            
        
        
        