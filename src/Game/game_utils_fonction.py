#utils functions that will be used in the OthelloGame class

def get_available_moves(state, player):
    """return the list of available moves for the current player""" 
    available_moves = []
    board_size = len(state)

    for row in range(board_size):
        for col in range(board_size):
            # check if the cell is empty
            if state[row][col] == 0:
                # check if the move is valid in any direction
                if is_valid_move(state, player, row, col):
                    available_moves.append((row, col))

    return available_moves


def get_flip_circles(state, row, col):
    """return the list of circles to flip""" 
    return []