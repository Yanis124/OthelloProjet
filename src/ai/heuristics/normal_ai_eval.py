# the static values of each square on the board
values = [
        [4, -3, 2, 2, 2, 2, -3, 4],
        [-3, -4, -1, -1, -1, -1, -4, -3],
        [2, -1, 1, 0, 0, 1, -1, 2],
        [2, -1, 0, 1, 1, 0, -1, 2],
        [2, -1, 0, 1, 1, 0, -1, 2],
        [2, -1, 1, 0, 0, 1, -1, 2],
        [-3, -4, -1, -1, -1, -1, -4, -3],
        [4, -3, 2, 2, 2, 2, -3, 4]
    ]

def normal_ai_utility(state, max_player_color, min_player_color):
    """return the evaluation of a position"""
    
    eval = 0
    
    for i in range(0,8):
        for j in range(0,8):
            if state[i][j] == max_player_color:
                eval += values[i][j]
            elif state[i][j] == min_player_color:
                eval -= values[i][j]
                
    return eval
    
    
    