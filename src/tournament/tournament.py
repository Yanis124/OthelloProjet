from src.Game.othello_game import OthelloGame

class Tournament:
    """simulate a tournament between the AI with different difficulty levels"""
    
    def __init__(self, first_ai_difficulty, second_ai_difficulty):
        
        self.first_ai_difficulty = first_ai_difficulty
        self.second_ai_difficulty = second_ai_difficulty
        self.game = None
        
    def ai_vs_ai(self, file_path):
        """run a game between two ia"""
        
        self.game = OthelloGame(None)
        
        self.first_ai_difficulty = self.first_ai_difficulty
        self.second_ai_difficulty = self.second_ai_difficulty
        
        result = self.game.ai_vs_ai(self.first_ai_difficulty, self.second_ai_difficulty)
        print("result: ", result)
        
        winner = self.first_ai_difficulty if result[0] > result[1] else (self.second_ai_difficulty if result[0] < result[1] else None)
            
        # Write the result to a text file
        with open(file_path, "a") as file:
            file.write(f"{winner, result[0], result[1]}\n")
            
    def simulate_tournament(self, file_path, nb_games):
        """simulate a tournament between the AI"""
        
        for i in range(nb_games):
            self.ai_vs_ai(file_path)

tournament = Tournament(0,1)
tournament.simulate_tournament("src/performance/easy_vs_normal.txt", 10)
    
        