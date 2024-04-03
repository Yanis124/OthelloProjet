#utils functions that will be used in the OthelloGame class
import cProfile

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
    """Check if placing a piece at (row, col) is a valid move for the player."""
    board_size = len(state)
    opponent = get_opponent_player(player)

    # directions to check: right, left, down, up, and diagonals
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    for d_row, d_col in directions:
        cur_row, cur_col = row + d_row, col + d_col
        found_opponent = False

        # move in the direction until we hit a piece of the player, or an empty cell or the edge of the board
        while 0 <= cur_row < board_size and 0 <= cur_col < board_size:
            if state[cur_row][cur_col] == opponent:
                found_opponent = True
            elif state[cur_row][cur_col] == player and found_opponent:
                # found a sequence of opponent pieces followed by a player's piece
                return True
            else:
                break

            # move to the next cell in the direction
            cur_row += d_row
            cur_col += d_col

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


