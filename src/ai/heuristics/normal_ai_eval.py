from src.ai.heuristics.easy_ai_eval import easy_ai_utility
from src.ai.heuristics.heuristique_utils_fonctions import circle_count

def moderate_eval_function(state, max_player_color, min_player_color):
    """return the evaluation of a position"""
                
    coins_parametres = circle_count(state, max_player_color, min_player_color)
    eval = easy_ai_utility(state, max_player_color, min_player_color)

    return eval + (coins_parametres[0] - coins_parametres[1])
    
    
    