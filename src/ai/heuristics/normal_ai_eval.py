from src.ai.heuristics.easy_ai_eval import easy_eval_function
from src.ai.heuristics.heuristique_utils_fonctions import circle_count

def moderate_eval_function(state, max_player_color, min_player_color):
    """
    Returns the evaluation of a position.

    This evaluation function combines the result of the easy AI utility function with the difference
    between the number of circles for the max player and the number of circles for the min player.

    Parameters:
    state : the current game state
    max_player_color : the color of the max player 
    min_player_color : the color of the min player 

    Returns:
    int: the evaluation of the position
    """
    coins_parametres = circle_count(state, max_player_color, min_player_color)  # get the number of circles for each player
    eval = easy_eval_function(state, max_player_color, min_player_color)  # get the evaluation using the easy AI utility function

    return eval + (coins_parametres[0] - coins_parametres[1])  # return the combined evaluation
