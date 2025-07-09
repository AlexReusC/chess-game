ROWS = 8
COLS = 8

class Board():
    def __init__(self):
        self._state = [[None] * COLS for _ in range(ROWS)]

    def get_piece_at_position(self, row, col):
        return self._state[row][col]

    def add_piece(self, piece):
        self._state[piece.row][piece.col] = piece

    def move_piece(self, source_row, source_col, dest_row, dest_col):
        if self._state[source_row][source_col]:
            self._state[dest_row][dest_col] = self._state[source_row][source_col]
            self._state[source_row][source_col] = None