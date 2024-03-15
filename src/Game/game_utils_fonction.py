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



def is_valid_move(state, player, row, col):
    """Check if the move is valid in any direction."""
    # check the bounds of the board
    if not (0 <= row < len(state) and 0 <= col < len(state)):
        return False
  
    if state[row][col] != 0:
        return False

    # check if the move is valid in any direction
    for d_row, d_col in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
        cur_row, cur_col = row + d_row, col + d_col
        found_opponent = False

        # check if there is an opponent's piece in the adjacent cell
        while 0 <= cur_row < len(state) and 0 <= cur_col < len(state) and state[cur_row][cur_col] == -player:
            cur_row += d_row
            cur_col += d_col
            found_opponent = True

        # if piece found and followed by the current player's piece => the move is valid
        if found_opponent and 0 <= cur_row < len(state) and 0 <= cur_col < len(state) and state[cur_row][cur_col] == player:
            return True

    # else return false
    return False


def get_flip_circles(state, row, col):
    """return the list of circles to flip""" 
    return []