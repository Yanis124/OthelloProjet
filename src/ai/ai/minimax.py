import random
from collections import Counter
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
    best_moves = []
    
    for move in get_available_moves(state, current_player_color):
        new_state = simulate_move(state, move, current_player_color)
        
        if current_player_color == max_player_color:
            eval = minimax(new_state, depth = depth, maximizing_player = False, max_player_color = max_player_color, min_player_color = min_player_color, utility_function = utility_function)
            print("move max player: ", move, eval, current_player_color, max_player_color, min_player_color)
            best_moves.append((move, eval))
                
        else:
            eval = minimax(new_state, depth = depth, maximizing_player = True, max_player_color = max_player_color, min_player_color = min_player_color, utility_function = utility_function)
            print("move min player: ", move, eval, current_player_color)
            best_moves.append((move, eval))
            
    if current_player_color == max_player_color:
        best_move = random.choice(select_highest_occurrences(best_moves)) #select reandom move from the list of best moves
        
    else :
        best_move = random.choice(select_lowest_occurrences(best_moves)) #select random move from the list of best moves
    
    print("best move : ", best_move[0], best_move[1], max_player_color, min_player_color, current_player_color)
    
    return best_move[0]
    
def select_highest_occurrences(lst):
    max_value = max(item[1] for item in lst)
    return [item for item in lst if item[1] == max_value]

def select_lowest_occurrences(lst):
    min_value = min(item[1] for item in lst)
    return [item for item in lst if item[1] == min_value]