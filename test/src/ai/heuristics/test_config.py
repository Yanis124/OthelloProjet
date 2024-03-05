#store positions of an othello game to test functions

state_full_board = [['black', 'black', 'black', 'black', 'black', 'black', 'black', 'black'],
             ['black', 'black', 'black', 'black', 'black', 'black', 'black', 'black'],
             ['black', 'black', 'black', 'black', 'black', 'black', 'black', 'black'],
             ['black', 'black', 'black', 'black', 'black', 'black', 'black', 'black'],
             ['black', 'black', 'black', 'black', 'white', 'white', 'white', 'white'],
             ['black', 'black', 'black', 'black', 'white', 'white', 'white', 'white'],
             ['black', 'black', 'black', 'black', 'white', 'white', 'white', 'white'],
             ['black', 'black', 'black', 'black', 'white', 'white', 'white', 'white']] #+32 black

state_initial_board = [[None, None, None, None, None, None, None, None],
             [None, None, None, None, None, None, None, None],
             [None, None, None, None, None, None, None, None],
             [None, None, None, 'white', 'black', None, None, None],
             [None, None, None, 'black', 'white', None,None , None],
             [None, None, None, None, None, None, None, None],
             [None, None, None, None, None, None, None, None],
             [None, None, None, None, None, None, None, None]] #+0

state_random_board = [
        ['black', 'black', 'white', None, 'white', 'black', None, 'black'],
        [None, 'white', 'white', 'black', 'white', None, 'black', None],
        ['black', 'white', 'black', None, 'black', None, 'white', 'white'],
        ['black', 'black', 'white', None, 'black', 'black', 'white', 'black'],
        ['white', 'black', None, 'black', 'black', 'white', None, 'white'],
        ['white', 'black', 'black', 'white', 'white', 'black', 'white', None],
        ['white', None, 'black', 'black', 'white', 'black', 'black', 'white'],
        ['white', 'white', 'white', 'black', None, 'white', 'white', 'black']] #+1 black