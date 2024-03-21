from src.ai.heuristics.easy_ai_eval import easy_ai_utility
from src.ai.heuristics.hard_ai_eval import hard_ai_utility
from src.Game.game_utils_fonction import get_available_moves
from src.Game.othello_game import is_game_over


# TODO : minimax function

def minimax(state, depth, maximizing_player, max_player_color, min_player_color):
    """ minimax function """
    if depth == 0 or is_game_over(state):
        return evaluate(state, max_player_color, min_player_color)
    
    if maximizing_player:
        max_eval = float('-inf')
        for move in get_available_moves(state, max_player_color):
            new_state = simulate_move(state, move, max_player_color)
            eval = minimax(new_state, depth-1, False, max_player_color, min_player_color)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in get_available_moves(state, min_player_color):
            new_state = simulate_move(state, move, min_player_color)
            eval = minimax(new_state, depth - 1, True, max_player_color, min_player_color)
            min_eval = min(min_eval, eval)
        return min_eval
    
    
def evaluate(state, max_player_color, min_player_color):
    """evaluate the current game state using heuristics functions"""
    return hard_ai_utility(state, max_player_color, min_player_color)


def simulate_move(state, move, player_color):
    """simulate a move to obtain a new game state"""

    new_state = deepcopy(state)
    row, col = move
    new_state[row][col] = player_color
    
    return new_state


def get_best_move(state, max_player_color, min_player_color):
    """return the best move to play, using minimax algo"""
    best_move = None
    best_eval = float('-inf')
    for move in get_available_moves(state, max_player_color):
        new_state = simulate_move(state, move, max_player_color)
        eval = minimax(new_state, depth=3, maximizing_player=False, max_player_color=max_player_color, min_player_color=min_player_color)
        if eval > best_eval:
            best_eval = eval
            best_move = move
    return best_move