from src.Game.othello_game import OthelloGame

class Tournament:
    """simulate a tournament between the AI with different difficulty levels"""
    
    def __init__(self):
        self.first_ai_difficulty = None
        self.second_ai_difficulty = None
        self.game = OthelloGame(None)
        
    def ai_vs_ai(self, first_ai_difficulty, second_ai_difficulty):
        """run a game between two ia"""
        
        self.first_ai_difficulty = first_ai_difficulty
        self.second_ai_difficulty = second_ai_difficulty
        
        result = self.game.ai_vs_ai(self.first_ai_difficulty, self.second_ai_difficulty)
        print("result: ", result)
        
        winner = first_ai_difficulty if result[0] > result[1] else (second_ai_difficulty if result[0] < result[1] else None)
            
        # Write the result to a text file
        with open("src/performance/easy_vs_normal.txt", "a") as file:
            file.write(f"{winner, result[0], result[1]}\n")
        
Tournament().ai_vs_ai(0, 1) # run a game between two AI with different difficulty levels (0 easy, 1 normal, 2 hard) 
    
        