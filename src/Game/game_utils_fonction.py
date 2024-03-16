#utils functions that will be used in the OthelloGame class

def get_available_moves(state, player):
    """return the list of available moves for the current player""" 
    available_moves = []
    board_size = len(state)

    for row in range(board_size):
        for col in range(board_size):
            # check if the cell is empty
            if state[row][col] == None:
                # check if the move is valid in any direction
                if is_valid_move(state, player, row, col):
                    available_moves.append((row, col))
                    
    print(available_moves)

    return available_moves



def is_valid_move(state, player, row, col):
    """Check if the move is valid in any direction."""
    # check the bounds of the board
    
    board_size = len(state)
    
    if not (row in range(board_size) and col in range(board_size)):
        return False
  
    if state[row][col] != None:
        return False
    
    opponent = get_opponent_player(player) 

    # check if the move is valid in any direction
    for d_row, d_col in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
        cur_row, cur_col = row + d_row, col + d_col
        found_opponent = False

        # check if there is an opponent's piece in the adjacent cell
        while cur_row in range(board_size) and cur_col in range(board_size) and state[cur_row][cur_col] == opponent:
            cur_row += d_row
            cur_col += d_col
            found_opponent = True

        # if piece found and followed by the current player's piece => the move is valid
        if found_opponent and cur_row in range(board_size) and cur_col in range(board_size) and state[cur_row][cur_col] == player:
            return True

    # else return false
    return False

def get_opponent_player(player):
    """return the opponent player"""
    return "black" if player == "white" else "white"