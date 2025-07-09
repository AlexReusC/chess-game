from __future__ import annotations

from abc import ABC, abstractmethod
from player import Player
import board


class Piece(ABC):
    
    @abstractmethod
    def __init__(self, owner, row, col):
        self.owner : Player = owner
        self.row = row
        self.col = col

    @abstractmethod
    def get_char(self) -> str:
        pass

    def change_position(self, row, col):
        self.row = row
        self.col = col

    @abstractmethod
    def get_possible_movements(self, board : board.Board):
        pass

    @abstractmethod
    def get_possible_kills(self, board):
        pass

class Pawn(Piece):
    def __init__(self, owner, row, col):
        super().__init__(owner, row, col)

    def get_char(self) -> str:
        if self.owner.is_white:
            return "♟"
        else:
            return "♙"

    def get_possible_movements(self, board):
        return [(4, 4)]

    def get_possible_kills(self, board):
        return [(4, 4)]

class Rook(Piece):
    def __init__(self, owner, row, col):
        super().__init__(owner, row, col)

    def get_char(self) -> str:
        if self.owner.is_white:
            return "♜"
        else:
            return "♖"

    def get_possible_movements(self, board):
        return [(4, 4)]

    def get_possible_kills(self, board):
        return [(4, 4)]

class Knight(Piece):
    movements = [(2, 1), (1, 2), (-2, 1), (1, -2), (2, -1), (-1, 2), (-2, -1), (-1, -2)]

    def __init__(self, owner, row, col):
        super().__init__(owner, row, col)

    def get_char(self) -> str:
        if self.owner.is_white:
            return "♞"
        else:
            return "♘"
        
    def get_possible_movements(self, board):
        possible_movements = []
        for row, col in self.movements:
            if board.get_piece_at_position(row + self.row, col + self.col) is None:
                possible_movements.append((row + self.row, col + self.col))

        return possible_movements
    
    def get_possible_kills(self, board):
        possible_kills = []
        for row, col in self.movements:
            piece_at_pos = board.get_piece_at_position(row + self.row, col + self.col)
            if piece_at_pos and piece_at_pos.owner != self.owner:
                possible_kills.append((row + self.row, col + self.col))

        return possible_kills

class Bishop(Piece):
    def __init__(self, owner, row, col):
        super().__init__(owner, row, col)

    def get_char(self) -> str:
        if self.owner.is_white:
            return "♝"
        else:
            return "♗"
        
    def get_possible_movements(self, board):
        return [(4, 4)]

    def get_possible_kills(self, board):
        return [(4, 4)]

class Queen(Piece):
    def __init__(self, owner, row, col):
        super().__init__(owner, row, col)   
    def get_char(self) -> str:
        if self.owner.is_white:
            return "♛"
        else:
            return "♕"

    def get_possible_movements(self, board):
        return [(4, 4)]

    def get_possible_kills(self, board):
        return [(5, 5)]

class King(Piece):
    def __init__(self, owner, row, col):
        super().__init__(owner, row, col)
    def get_char(self) -> str:
        if self.owner.is_white:
            return "♚"
        else:
            return "♔"
    def get_possible_movements(self, board):
        return [(4, 4)]
    
    def get_possible_kills(self, board):
        return [(5, 5)]