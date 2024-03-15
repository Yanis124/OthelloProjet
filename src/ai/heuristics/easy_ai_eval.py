from src.ai.heuristics.heuristique_utils_fonctions import circle_count

def easy_ai_utility(state, max_player_color, min_player_color):
    """return the evaluation of a position"""
     
    return circle_count(state, max_player_color, min_player_color)


def easy_ai(state, max_player_color, min_player_color):
    """choose a move based on the evaluation function"""
    available_moves = get_available_moves(state, max_player_color)
    best_move = None
    best_score = float('-inf')  
    
    for move in available_moves:
        new_state = apply_move(state, move, max_player_color)
        score = easy_ai_utility(new_state, max_player_color, min_player_color)
        
        if score > best_score:
            best_score = score
            best_move = move
    
    return best_move