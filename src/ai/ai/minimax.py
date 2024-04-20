import random
from collections import Counter
from copy import deepcopy
from src.Game.game_utils_fonction import get_available_moves
from src.Game.game_utils_fonction import is_game_over, get_flip_circles


def max_value(state, depth, alpha, beta, max_player_color, min_player_color, utility_function, use_alpha_beta=True, nodes_visited=0):
    if depth <= 0 or is_game_over(state):
        return utility_function(state, max_player_color, min_player_color), nodes_visited

    v = float('-inf')
    for move in get_available_moves(state, max_player_color):
        new_state = simulate_move(state, move, max_player_color)
        eval, nodes_visited = min_value(new_state, depth-1, alpha, beta, max_player_color, min_player_color, utility_function, use_alpha_beta, nodes_visited+1)
        v = max(v, eval)
        alpha = max(alpha, v)

        if use_alpha_beta and beta <= alpha:
            break

    return v, nodes_visited



def min_value(state, depth, alpha, beta, max_player_color, min_player_color, utility_function, use_alpha_beta=True, nodes_visited=0):
    if depth <= 0 or is_game_over(state):
        return utility_function(state, max_player_color, min_player_color), nodes_visited

    v = float('inf')
    for move in get_available_moves(state, min_player_color):
        new_state = simulate_move(state, move, min_player_color)
        eval, nodes_visited = max_value(new_state, depth-1, alpha, beta, max_player_color, min_player_color, utility_function, use_alpha_beta, nodes_visited+1)
        v = min(v, eval)
        beta = min(beta, v)

        if use_alpha_beta and beta <= alpha:
            break

    return v, nodes_visited

    
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
    best_eval = float('-inf') if current_player_color == max_player_color else float('inf')
    best_nodes_visited = 0

    for move in get_available_moves(state, current_player_color):
        new_state = simulate_move(state, move, current_player_color)

        if use_alpha_beta:
            if current_player_color == max_player_color:
                eval, nodes_visited = min_value(new_state, depth - 1, float('-inf'), float('inf'), max_player_color, min_player_color, utility_function, use_alpha_beta)
            else:
                eval, nodes_visited = max_value(new_state, depth - 1, float('-inf'), float('inf'), max_player_color, min_player_color, utility_function, use_alpha_beta)
        else:
            eval, nodes_visited = utility_function(new_state, max_player_color, min_player_color), 1

        if (current_player_color == max_player_color and eval > best_eval) or (current_player_color == min_player_color and eval < best_eval):
            best_move = move
            best_eval = eval
            best_nodes_visited = nodes_visited

    return best_move, best_nodes_visited





    
def select_highest_occurrences(lst):
    max_value = max(item[1] for item in lst)
    return [item for item in lst if item[1] == max_value]

def select_lowest_occurrences(lst):
    min_value = min(item[1] for item in lst)
    return [item for item in lst if item[1] == min_value]