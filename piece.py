from abc import ABC, abstractmethod
from player import Player

class Piece(ABC):
    
    @abstractmethod
    def __init__(self, owner, row, col):
        self.owner : Player = owner
        self.row = row
        self.col = col

    @abstractmethod
    def get_char(self) -> str:
        pass

    def get_possible_movements(self):
        pass

    def get_possible_kills(self):
        pass

class Pawn(Piece):
    def __init__(self, owner, row, col):
        super().__init__(owner, row, col)

    def get_char(self) -> str:
        if self.owner.is_white:
            return "♟"
        else:
            return "♙"


class Rook(Piece):
    def __init__(self, owner, row, col):
        super().__init__(owner, row, col)

    def get_char(self) -> str:
        if self.owner.is_white:
            return "♜"
        else:
            return "♖"

class Knight(Piece):
    def __init__(self, owner, row, col):
        super().__init__(owner, row, col)

    def get_char(self) -> str:
        if self.owner.is_white:
            return "♞"
        else:
            return "♘"

class Bishop(Piece):
    def __init__(self, owner, row, col):
        super().__init__(owner, row, col)

    def get_char(self) -> str:
        if self.owner.is_white:
            return "♝"
        else:
            return "♗"

class Queen(Piece):
    def __init__(self, owner, row, col):
        super().__init__(owner, row, col)   
    def get_char(self) -> str:
        if self.owner.is_white:
            return "♛"
        else:
            return "♕"

class King(Piece):
    def __init__(self, owner, row, col):
        super().__init__(owner, row, col)
    def get_char(self) -> str:
        if self.owner.is_white:
            return "♚"
        else:
            return "♔"