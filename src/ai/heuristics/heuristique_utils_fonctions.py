from src.Game.game_utils_fonction import get_available_moves

def circle_count(state, max_player_color, min_player_color):
    """return the difference between the circle number of the max player and the min player"""
    
    max_player_number_circle = 0
    min_player_number_circle = 0
    for row in state:
        for cell in row:
            if cell == max_player_color:
                 max_player_number_circle += 1
            elif cell == min_player_color:
                min_player_number_circle += 1
    
    return max_player_number_circle - min_player_number_circle

def circle_count_corner(state, max_player_color, min_player_color):
    """return the difference between the circle number in the corner of the max player and the min player"""
    
    max_player_number_circle = sum(1 for corner in [(0, 0), (0, 7), (7, 0), (7, 7)] if state[corner[0]][corner[1]] == max_player_color)
    min_player_number_circle = sum(1 for corner in [(0, 0), (0, 7), (7, 0), (7, 7)] if state[corner[0]][corner[1]] == min_player_color)
    
    return max_player_number_circle - min_player_number_circle

def mobility(state, max_player_color, min_player_color):
    """return the diference of mobility between the max and min player """
    
    return len(get_available_moves(state, max_player_color)) -len(get_available_moves(state, min_player_color))
    
def stability(state, max_player_color, min_player_color):
    """return the difference between the stability of the max player and the min player"""
    
    
    