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

def easy_eval_function(state, max_player_color, min_player_color):
    """Return the evaluation of a position"""
    
    eval = 0 
    
    for i in range(0, 8):
        for j in range(0, 8):
            if state[i][j] == max_player_color:  # if the cell belongs to the max player
                eval += values[i][j]  # add the value of the cell to the evaluation
            elif state[i][j] == min_player_color:  # if the cell belongs to the min player
                eval -= values[i][j]  # subtract the value of the cell from the evaluation
     
    return eval  # return the evaluation
