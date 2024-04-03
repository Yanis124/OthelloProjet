from src.ai.heuristics.heuristique_utils_fonctions import circle_count, circle_count_corner, mobility, stability 

def calculate_heuristique_score(max_player_parametre, min_player_parametre):
    """return thes score of an heuristique (coin parity, mobility, stability ...)"""
    
    if (max_player_parametre + min_player_parametre == 0) or (max_player_parametre - min_player_parametre == 0): #if both parametres we return 0 for that heuristique /0(not allowed !)
        return 0
    
    
    return 100 * (max_player_parametre - min_player_parametre) / abs(max_player_parametre + min_player_parametre)# Using abs ensures stability evaluation remains consistent even if one player's value is negative.

def hard_ai_utility(state, max_player_color, min_player_color):
    max_coins, min_coins = circle_count(state, max_player_color, min_player_color)
    max_mobility, min_mobility = mobility(state, max_player_color, min_player_color)
    max_corners, min_corners = circle_count_corner(state, max_player_color, min_player_color)
    max_stability, min_stability = stability(state, max_player_color, min_player_color)

    coin_score = calculate_heuristique_score(max_coins, min_coins)
    mobility_score = calculate_heuristique_score(max_mobility, min_mobility)
    corner_score = calculate_heuristique_score(max_corners, min_corners)
    stability_score = calculate_heuristique_score(max_stability, min_stability)

    return coin_score + mobility_score + corner_score + stability_score
