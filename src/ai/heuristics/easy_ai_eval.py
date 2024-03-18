from src.ai.heuristics.heuristique_utils_fonctions import circle_count, get_available_moves

def easy_ai_utility(state, max_player_color, min_player_color):
    """return the evaluation of a position"""
    
    coins_parametres =  circle_count(state, max_player_color, min_player_color)
     
    return coins_parametres[0] - coins_parametres[1]

