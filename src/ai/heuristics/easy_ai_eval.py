from src.ai.heuristics.heuristique_utils_fonctions import circle_count

def easy_ai_utility(state, max_player_color, min_player_color):
    """return the evaluation of a position"""
     
    return circle_count(state, max_player_color, min_player_color)