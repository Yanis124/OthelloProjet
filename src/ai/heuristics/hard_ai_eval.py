from src.ai.heuristics.heuristique_utils_fonctions import circle_count, circle_count_corner, mobility, stability 


def calculate_heuristic_score(max_player_parametre, min_player_parametre):
    """
    Returns the score of a heuristic (coin parity, mobility, stability, etc.)

    The score is calculated as the difference between the max player's parameter and the min player's parameter,
    normalized by the sum of the two parameters.

    Parameters:
    max_player_parametre (int): the value of the heuristic parameter for the max player
    min_player_parametre (int): the value of the heuristic parameter for the min player

    Returns:
    int: the score of the heuristic, ranging from -100 to 100
    """

    if (max_player_parametre + min_player_parametre == 0) or (max_player_parametre - min_player_parametre == 0):
        return 0

    return 100 * (max_player_parametre - min_player_parametre) / abs(max_player_parametre + min_player_parametre)


def hard_eval_function(state, max_player_color, min_player_color):
    """
    Returns the utility value of a given game state for the hard AI player.

    The utility value is calculated as the sum of the scores of four heuristics:
    coin parity, mobility, corner control, and stability.

    Parameters:
    state (list of lists): the current game state
    max_player_color (str): the color of the hard AI player 
    min_player_color (str): the color of the opponent player 

    Returns:
    int: the utility value of the game state for the hard AI player
    """
    max_coins, min_coins = circle_count(state, max_player_color, min_player_color)
    max_mobility, min_mobility = mobility(state, max_player_color, min_player_color)
    max_corners, min_corners = circle_count_corner(state, max_player_color, min_player_color)
    max_stability, min_stability = stability(state, max_player_color, min_player_color)

    coin_score = calculate_heuristique_score(max_coins, min_coins)
    mobility_score = calculate_heuristique_score(max_mobility, min_mobility)
    corner_score = calculate_heuristique_score(max_corners, min_corners)
    stability_score = calculate_heuristique_score(max_stability, min_stability)

    return coin_score + mobility_score + corner_score + stability_score
