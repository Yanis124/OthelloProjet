from src.Game.othello_game import OthelloGame

class Tournament:
    """simulate a tournament between the AI with different difficulty levels"""
    
    def __init__(self, first_ai_difficulty, second_ai_difficulty, first_ai_elagage, second_ai_elagage):
        
        self.first_ai_difficulty = first_ai_difficulty
        self.second_ai_difficulty = second_ai_difficulty
        self.first_ai_elagage = first_ai_elagage
        self.second_ai_elagage = second_ai_elagage
        self.game = None
        
    def ai_vs_ai(self, file_path):
        """run a game between two ia"""
        
        self.game = OthelloGame(None)
        
        self.first_ai_difficulty = self.first_ai_difficulty
        self.second_ai_difficulty = self.second_ai_difficulty
        
        result = self.game.ai_vs_ai()
        print("result: ", result)
        
        winner = self.first_ai_difficulty if result[0] > result[1] else (self.second_ai_difficulty if result[0] < result[1] else None)
            
        # Write the result to a text file
        with open(file_path, "a") as file:
            file.write(f"{winner, result[0], result[1]}\n")
            
    def simulate_tournament(self, file_path, nb_games):
        """simulate a tournament between the AI"""
        
        for i in range(nb_games):
            self.ai_vs_ai(file_path)
            
    def simulate_game(self):
        """simulate a game between two to determine the number of node explored"""
        
        self.game = OthelloGame(None)
        
        self.game.ai_vs_ai(self.first_ai_difficulty, self.second_ai_difficulty, self.first_ai_elagage, self.second_ai_elagage)
        

tournament = Tournament(2, 2, True, False)
tournament.simulate_game()
    
        