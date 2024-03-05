
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
    
    max_player_number_circle = 0
    min_player_number_circle = 0
    for i in range(0, 8):
        for j in range(0, 8):
            if (i,j) in [(0,0), (0,7), (7,0), (7,7)]:
                if state[i][j] == max_player_color:
                    max_player_number_circle += 1
                elif state[i][j] == min_player_color:
                    min_player_number_circle += 1
                
    return max_player_number_circle - min_player_number_circle

def mobility(available_moves, current_player_color, max_player_color, min_player_color):
    """return the number of available move of the current player"""
    
    if current_player_color == max_player_color:
        return len(available_moves)
    
    elif current_player_color == min_player_color:
        return -len(available_moves)
    
def stability(state, max_player_color, min_player_color):
    """return the difference between the stability of the max player and the min player"""
    
    