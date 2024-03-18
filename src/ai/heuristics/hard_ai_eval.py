from src.ai.heuristics.heuristique_utils_fonctions import circle_count, circle_count_corner, mobility, stability 

def calculate_heuristique_score(max_player_parametre, min_player_parametre):
    """return thes score of an heuristique (coin parity, mobility, stability ...)"""
    
    if max_player_parametre + min_player_parametre == 0: #if both parametres we return 0 for that heuristique /0(not allowed !)
        return 0
    
    return 100 * (max_player_parametre - min_player_parametre) / abs(max_player_parametre + min_player_parametre)# Using abs ensures stability evaluation remains consistent even if one player's value is negative.

def hard_ai_utility(state, max_player_color, min_player_color):
    """return the evaluation of a position"""
    
    #get max_player and min_player value for each heuristique
    coins_parametres =  circle_count(state, max_player_color, min_player_color)
    mobility_parametres = mobility(state, max_player_color, min_player_color)
    corner_parametres = circle_count_corner(state, max_player_color, min_player_color)
    stability_parametres = stability(state, max_player_color, min_player_color)
    
    #applie the formula to get the value if each heuristique
    coin_score = calculate_heuristique_score(coins_parametres[0], coins_parametres[1])
    mobility_score = calculate_heuristique_score(mobility_parametres[0], mobility_parametres[1])
    corner_score = calculate_heuristique_score(corner_parametres[0], corner_parametres[1])
    stability_score = calculate_heuristique_score(stability_parametres[0], stability_parametres[1])
    
    return coin_score + mobility_score + corner_score + stability_score
    
        
    
        