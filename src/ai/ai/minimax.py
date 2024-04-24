import random
from collections import Counter
from copy import deepcopy
from src.Game.game_utils_fonction import get_available_moves
from src.Game.game_utils_fonction import is_game_over, get_flip_circles


def max_value(state, depth, alpha, beta, max_player_color, min_player_color, utility_function, use_alpha_beta=True):
    if depth <= 0 or is_game_over(state):
        return utility_function(state, max_player_color, min_player_color)
    
    v = float('-inf')
    for move in get_available_moves(state, max_player_color):
        new_state = simulate_move(state, move, max_player_color)
        v = max(v, min_value(new_state, depth-1, alpha, beta, max_player_color, min_player_color, utility_function, use_alpha_beta)) 
        #print(move, depth)
        alpha = max(alpha, v)
        
        if use_alpha_beta and beta <= alpha:
            #print(f"Élagage dans MAX à profondeur {depth}, coup: {move}, alpha: {alpha}, beta: {beta}")
            return v

    return v

def min_value(state, depth, alpha, beta, max_player_color, min_player_color, utility_function, use_alpha_beta=True):
    if depth <= 0 or is_game_over(state):
        return utility_function(state, max_player_color, min_player_color)
    
    v = float('inf')
    for move in get_available_moves(state, min_player_color):
        new_state = simulate_move(state, move, min_player_color)
        v = min(v, max_value(new_state, depth-1, alpha, beta, max_player_color, min_player_color, utility_function, use_alpha_beta)) 
        #print(move, depth)
        
        beta = min(beta, v)
        if use_alpha_beta and beta <= alpha:
            #print(f"Élagage dans MIN à profondeur {depth}, coup: {move}, alpha: {alpha}, beta: {beta}")
            return v
        
    return v
    
def simulate_move(state, move, player_color):
    """simulate a move to obtain a new game state"""

    new_state = deepcopy(state)
    row, col = move
    new_state[row][col] = player_color # place the piece on the board
    
    fliped_circles = get_flip_circles(state, player_color, row, col)
    
    for c in fliped_circles:
        new_state[c[0]][c[1]] = player_color  #flip the captured pieces
    
    return new_state



def get_best_move(state, max_player_color, min_player_color, current_player_color, depth, utility_function, use_alpha_beta=True):
    best_move = None
    best_moves = []
    
    for move in get_available_moves(state, current_player_color):
        new_state = simulate_move(state, move, current_player_color)
        
        # init alpha et beta seulement si use_alpha_beta est True
        alpha = float('-inf') 
        beta = float('inf') 
         
        if current_player_color == max_player_color:
            eval = min_value(new_state, depth - 1, alpha, beta, max_player_color, min_player_color, utility_function, use_alpha_beta) # appel de min_value pour le joueur min
        else:
            eval = max_value(new_state, depth - 1, alpha, beta, max_player_color, min_player_color, utility_function, use_alpha_beta) # appel de max_value pour le joueur max 
        
        if current_player_color == max_player_color:
            eval = min_value(new_state, depth - 1, alpha, beta, max_player_color, min_player_color, utility_function, use_alpha_beta) # appel de min_value pour le joueur min
        else:
            eval = max_value(new_state, depth - 1, alpha, beta, max_player_color, min_player_color, utility_function, use_alpha_beta) # appel de max_value pour le joueur max
        
        best_moves.append((move, eval))  # Adds the movement and its rating to the list of best movements
    
    if current_player_color == max_player_color:
        best_moves = select_highest_occurrences(best_moves)
    else:
        best_moves = select_lowest_occurrences(best_moves)

    best_move = random.choice(best_moves)[0]  # Choose randomly from the best movements
    
    return best_move

def select_highest_occurrences(lst):
    max_value = max(item[1] for item in lst)
    return [item for item in lst if item[1] == max_value]

def select_lowest_occurrences(lst):
    min_value = min(item[1] for item in lst)
    return [item for item in lst if item[1] == min_value]
