from typing import List
import piece
ROWS = 8
COLS = 8

class Board():
    def __init__(self):
        self._state : List[List[piece.Piece | None]]  = [[None] * COLS for _ in range(ROWS)]

    def get_piece_at_position(self, row, col):
        if 0 <= row < ROWS and 0 <= col < COLS:
            return self._state[row][col]
        return None

    def add_piece(self, piece):
        self._state[piece.row][piece.col] = piece

    def get_possible_movements(self, row, col):
        if self._state[row][col]:
            return self._state[row][col].get_possible_movements(self)
        return []
    
    def get_possible_kills(self, row, col):
        if self._state[row][col]:
            return self._state[row][col].get_possible_kills(self)
        return []

    def move_piece(self, source_row, source_col, dest_row, dest_col):
        if self._state[source_row][source_col]:
            self._state[dest_row][dest_col] = self._state[source_row][source_col]
            self._state[dest_row][dest_col].change_position(dest_row, dest_col)
            self._state[source_row][source_col] = None