from copy import deepcopy
from src.Game.game_utils_fonction import get_available_moves
from src.Game.game_utils_fonction import is_game_over, get_flip_circles

def minimax(state, depth, maximizing_player, max_player_color, min_player_color, utility_function):
    """ minimax function """
    
    if depth == 0 or is_game_over(state):
        return utility_function(state, max_player_color, min_player_color)
    
    if maximizing_player:
        max_eval = float('-inf')
        for move in get_available_moves(state, max_player_color):
            new_state = simulate_move(state, move, max_player_color)
            eval = minimax(new_state, depth-1, False, max_player_color, min_player_color, utility_function)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in get_available_moves(state, min_player_color):
            new_state = simulate_move(state, move, min_player_color)
            eval = minimax(new_state, depth - 1, True, max_player_color, min_player_color, utility_function)
            min_eval = min(min_eval, eval)
        return min_eval
    
def simulate_move(state, move, player_color):
    """simulate a move to obtain a new game state"""

    new_state = deepcopy(state)
    row, col = move
    new_state[row][col] = player_color # place the piece on the board
    
    fliped_circles = get_flip_circles(state, player_color, row, col)
    
    for c in fliped_circles:
        new_state[c[0]][c[1]] = player_color  #flip the captured pieces
    
    return new_state


def get_best_move(state, max_player_color, min_player_color, current_player_color, depth, utility_function):
    """return the best move to play, using minimax algo"""
    best_move = None
    best_eval_min_player = float('inf')
    best_eval_max_player = float('-inf')
    best_eval = None
    
    for move in get_available_moves(state, current_player_color):
        new_state = simulate_move(state, move, current_player_color)
        
        if current_player_color == max_player_color:
            eval = minimax(new_state, depth = depth, maximizing_player = False, max_player_color = max_player_color, min_player_color = min_player_color, utility_function = utility_function)
        
            #if the current player is max we will return the moe with the highest evaluation
            if eval > best_eval_max_player :
                best_eval = eval
                best_move = move
                
        else:
            eval = minimax(new_state, depth = depth, maximizing_player = True, max_player_color = max_player_color, min_player_color = min_player_color, utility_function = utility_function)
            
        #if the current player is min we will return the moe with the lowest evaluation
            if eval < best_eval_min_player :
                best_eval = eval
                best_move = move
                
    print("best move : ", best_move, best_eval, min_player_color, max_player_color)
    
    return best_move
    
