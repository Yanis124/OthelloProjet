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
                    
    return available_moves



def is_valid_move(state, player, row, col):
    """Check if the move is valid in any direction."""
    # check the bounds of the board
    
    board_size = len(state)
    
    opponent = get_opponent_player(player) 

    # Check if there is at least one opponent's piece adjacent to the cell
    adjacent_opponent = False
    for d_row, d_col in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
        adj_row, adj_col = row + d_row, col + d_col
        if adj_row in range(board_size) and adj_col in range(board_size) and state[adj_row][adj_col] == opponent :
            adjacent_opponent = True
            break
    
    # if it not adjacent to an opponent's piece, the move is invalid
    if not adjacent_opponent:
        return False
    
    # Check if there is a sequence of opponent's pieces followed by the player's piece in any direction
    for d_row, d_col in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
        cur_row, cur_col = row + d_row, col + d_col
        found_opponent = False

        while 0 <= cur_row < len(state) and 0 <= cur_col < len(state[0]) and state[cur_row][cur_col] == opponent and state[cur_row][cur_col] is not None:
            cur_row += d_row
            cur_col += d_col
            found_opponent = True

        if found_opponent and 0 <= cur_row < len(state) and 0 <= cur_col < len(state[0]) and state[cur_row][cur_col] == player:
            return True

    return False

def get_flip_circles(state, player_color, row, col):
    """return the list of circles that will be flipped

        Args:
            row: The row index of the move.
            col: The column index of the move.
    """
    opponent_color = get_opponent_player(player_color)
        
    board_size = len(state)
    flipped_circle = []
        
    # check all directions
    for d_row, d_col in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
        cur_row, cur_col = row + d_row, col + d_col
        found_opponent = False
        to_flip = []

        # check if the bounds of the grid and the cell at (cur_row, cur_col) contains the opponent's color
        while cur_row in range(board_size) and cur_col in range(board_size) and state[cur_row][cur_col] == opponent_color:
            to_flip.append((cur_row, cur_col))
            cur_row += d_row
            cur_col += d_col
            found_opponent = True

            # if piece found and followed by the current player's piece => the move is valid and flip the pieces
            if found_opponent and cur_row in range(board_size) and cur_col in range(board_size) and state[cur_row][cur_col] == player_color:
                for flip_row, flip_col in to_flip:
                    flipped_circle.append((flip_row, flip_col))
                    
    return flipped_circle

def is_game_over(available_moves):
        """check if the game is over"""
        
        if len(available_moves) == 0:
            return True
        
        return False
    
def get_opponent_player(player):
    """return the opponent player"""
    return "black" if player == "white" else "white"