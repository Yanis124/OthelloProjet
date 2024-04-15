from src.Game.game_utils_fonction import get_available_moves


def circle_count(state, max_player_color, min_player_color):
    """ return a list the first variable is max_player number of circle the second one is min player number circle """
    max_player_number_circle = sum(1 for row in state for cell in row if cell == max_player_color)
    min_player_number_circle = sum(1 for row in state for cell in row if cell == min_player_color)
    return [max_player_number_circle, min_player_number_circle]




def circle_count_corner(state, max_player_color, min_player_color):
    """return a list the first variable is max_player mobility the second one is min player mobility """
    
    max_player_number_circle = sum(1 for corner in [(0, 0), (0, 7), (7, 0), (7, 7)] if state[corner[0]][corner[1]] == max_player_color)
    min_player_number_circle = sum(1 for corner in [(0, 0), (0, 7), (7, 0), (7, 7)] if state[corner[0]][corner[1]] == min_player_color)
    
    return [max_player_number_circle, min_player_number_circle]



def mobility(state, max_player_color, min_player_color):
    """return a list the first variable is max_player number of corner the second one is min_player number of corner"""
    
    return [len(get_available_moves(state, max_player_color)), len(get_available_moves(state, min_player_color))]
    
def stability(state, max_player_color, min_player_color):
    """return a list the first variable is max_player stability the second one is min player stability"""
    
    stability_max_player = 0
    stability_min_player = 0
    
    for row in range(len(state)):
        for col in range(len(state)):
            
            if(state[row][col] == max_player_color):
                if is_stable(state, max_player_color, row, col):
                    stability_max_player += 1
                else:
                    stability_max_player -= -1
                    
            elif(state[row][col] == min_player_color):
                if is_stable(state, min_player_color, row, col):
                    stability_min_player += 1
                else:
                    stability_min_player -= -1
        
    return [stability_max_player, stability_min_player]
    
def is_stable(state, player, row, col):
    """return True if the piece is stable
    a piece is stable if it is in a corner or if it is on the edge of the board"""    
    
    if ((row == 0 or row == len(state) - 1) or (col == 0 or col == (len(state) - 1))) and state[row][col] == player:
        return True

    return False    


def controlled_central_squares(state, max_player_color, min_player_color):
    """returns a list the first variables is the number of pieces controlled by the max player and the seconde variable is the min player central squares pieces"""
    
    central_squares = [(2, 2), (2, 3), (2, 4), (3, 2), (3, 3), (3, 4), (4, 2), (4, 3), (4, 4)]
    max_player_count = 0
    min_player_count = 0
    
    for row, col in central_squares:
        if state[row][col] == max_player_color:
            max_player_count += 1
        elif state[row][col] == min_player_color:
            min_player_count += 1
    
    return [max_player_count, min_player_count]
