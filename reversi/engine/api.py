import engine.player as player

# WHITE = -1
# BLACK = 1

INIT_BOARD = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 1, 0, 0, 0],
    [0, 0, 0, 1, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]

COLOR_MAP = {
        0: 0,
        1: 1,
        2: -1,
    }

def get_next_board(board, color):
    color = COLOR_MAP[color]
    moves = player.possible_moves(board[:], color)
    if len(moves):
        features = player.calculate_board_features(board[:])
        move = player.alphabeta_table(
            board[:], features, 5, -100000, 100000, color, color, 0, board.count(0)
        )[1]
        new_board = player.attempt_to_make_move(move, board[:], color)
    else:
        new_board = board
    return new_board


def is_valid_move(move, board, color):
    color = COLOR_MAP[color]
    return player.is_legal_move(move, board[:], color)
