from typing import List
from piece import Piece
ROWS = 8
COLS = 8

class Board():
    def __init__(self):
        self._state : List[List[Piece | None]]  = [[None] * COLS for _ in range(ROWS)]

    def get_piece_at_position(self, row, col):
        return self._state[row][col]

    def add_piece(self, piece):
        self._state[piece.row][piece.col] = piece

    def get_possible_movements(self, row, col):
        if self._state[row][col]:
            return self._state[row][col].get_possible_movements()
        return []
    
    def get_possible_kills(self, row, col):
        if self._state[row][col]:
            return self._state[row][col].get_possible_kills()
        return []

    def move_piece(self, source_row, source_col, dest_row, dest_col):
        if self._state[source_row][source_col]:
            self._state[dest_row][dest_col] = self._state[source_row][source_col]
            self._state[source_row][source_col] = None