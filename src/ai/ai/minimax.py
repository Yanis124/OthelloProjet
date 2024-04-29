import random
from collections import Counter
from copy import deepcopy
from src.Game.game_utils_fonction import get_available_moves
from src.Game.game_utils_fonction import is_game_over, get_flip_circles

def minimax_decision(state, max_player_color, min_player_color, current_player_color, depth, utility_function, use_alpha_beta=True):
    """
    Returns the best move for the current player using the minimax algorithm.
    """
    best_move = None
    best_moves = []

    # iterate through all possible moves for the current player
    for move in get_available_moves(state, current_player_color):
        new_state = simulate_move(state, move, current_player_color)  # simulate the move
        
        # initialize alpha and beta only if use_alpha_beta is True
        alpha = float('-inf')
        beta = float('inf')

        if current_player_color == max_player_color:
            # call min_value for the min player
            eval = min_value(new_state, depth - 1, alpha, beta, max_player_color, min_player_color, utility_function, use_alpha_beta)
        else:
            # call max_value for the max player
            eval = max_value(new_state, depth - 1, alpha, beta, max_player_color, min_player_color, utility_function, use_alpha_beta)

        best_moves.append((move, eval))  # add the move and its evaluation to the list of best moves

    if current_player_color == max_player_color:
        best_moves = select_highest_occurrences(best_moves)  # select the highest occurrences
    else:
        best_moves = select_lowest_occurrences(best_moves)  # select the lowest occurrences

    best_move = random.choice(best_moves)[0]  # randomly choose from the best moves

    return best_move


def max_value(state, depth, alpha, beta, max_player_color, min_player_color, utility_function, use_alpha_beta=True):
    """
    Returns the maximum value that the max player can obtain.
    """
    # if we've reached the maximum depth or the game is over, return the utility value
    if depth <= 0 or is_game_over(state):
        return utility_function(state, max_player_color, min_player_color)

    v = float('-inf') 
    for move in get_available_moves(state, max_player_color):
        new_state = simulate_move(state, move, max_player_color)  # simulate the move
        # recursively find the minimum value for the min player
        v = max(v, min_value(new_state, depth-1, alpha, beta, max_player_color, min_player_color, utility_function, use_alpha_beta))
        alpha = max(alpha, v)  # update alpha with the maximum value found so far

        # if alpha-beta pruning is enabled and beta is less than or equal to alpha, prune
        if use_alpha_beta and beta <= alpha:
            return v  # prune and return the current value

    return v  # returns the maximum value found


def min_value(state, depth, alpha, beta, max_player_color, min_player_color, utility_function, use_alpha_beta=True):
    """
    Returns the minimum value that the min player can obtain.
    """
    # if we've reached the maximum depth or the game is over, return the utility value
    if depth <= 0 or is_game_over(state):
        return utility_function(state, max_player_color, min_player_color)

    v = float('inf')  
    for move in get_available_moves(state, min_player_color):
        new_state = simulate_move(state, move, min_player_color)  # simulate the move
        # recursively find the maximum value for the max player
        v = min(v, max_value(new_state, depth-1, alpha, beta, max_player_color, min_player_color, utility_function, use_alpha_beta))
        beta = min(beta, v)  # update beta with the minimum value found so far

        # if alpha-beta pruning is enabled and beta is less than or equal to alpha, prune
        if use_alpha_beta and beta <= alpha:
            return v  # prune and return the current value

    return v  # return the minimum value found


def simulate_move(state, move, player_color):
    """
    Simulates a move to obtain a new game state.
    """
    new_state = deepcopy(state)  # create a deep copy of the current game state           ??? optimize perf
    row, col = move  # extract the row and column of the move
    new_state[row][col] = player_color  # place the player's piece on the board

    fliped_circles = get_flip_circles(state, player_color, row, col)  # get the circles to be flipped

    for c in fliped_circles:
        new_state[c[0]][c[1]] = player_color  # flip the captured pieces by setting them to the player's color

    return new_state  # return the new game state after the move



def select_highest_occurrences(lst):
    """
    Returns the items with the highest occurrences in a list.
    """
    max_value = max(item[1] for item in lst)
    return [item for item in lst if item[1] == max_value]

def select_lowest_occurrences(lst):
    """
    Returns the items with the lowest occurrences in a list.
    """
    min_value = min(item[1] for item in lst)
    return [item for item in lst if item[1] == min_value]
