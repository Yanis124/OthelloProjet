
def circle_count(state, max_player_color, min_player_color):
    """return the difference between the circle number of the max player and the min player"""
    
    max_player_number_circle = 0
    min_player_number_circle = 0
    for row in state:
        for cell in row:
            if cell == max_player_color:
                 max_player_number_circle+= 1
            elif cell == min_player_color:
                min_player_number_circle += 1
                
    return max_player_number_circle - min_player_number_circle