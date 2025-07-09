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

    @abstractmethod
    def get_possible_movements(self):
        pass

    @abstractmethod
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

    def get_possible_movements(self):
        return [(4, 4)]

    def get_possible_kills(self):
        return [(4, 4)]

class Rook(Piece):
    def __init__(self, owner, row, col):
        super().__init__(owner, row, col)

    def get_char(self) -> str:
        if self.owner.is_white:
            return "♜"
        else:
            return "♖"

    def get_possible_movements(self):
        return [(4, 4)]

    def get_possible_kills(self):
        return [(4, 4)]

class Knight(Piece):
    def __init__(self, owner, row, col):
        super().__init__(owner, row, col)

    def get_char(self) -> str:
        if self.owner.is_white:
            return "♞"
        else:
            return "♘"
        
    def get_possible_movements(self):
        return [(4, 4)]
    
    def get_possible_kills(self):
        return [(4, 4)]

class Bishop(Piece):
    def __init__(self, owner, row, col):
        super().__init__(owner, row, col)

    def get_char(self) -> str:
        if self.owner.is_white:
            return "♝"
        else:
            return "♗"
        
    def get_possible_movements(self):
        return [(4, 4)]

    def get_possible_kills(self):
        return [(4, 4)]

class Queen(Piece):
    def __init__(self, owner, row, col):
        super().__init__(owner, row, col)   
    def get_char(self) -> str:
        if self.owner.is_white:
            return "♛"
        else:
            return "♕"

    def get_possible_movements(self):
        return [(4, 4)]

    def get_possible_kills(self):
        return [(5, 5)]

class King(Piece):
    def __init__(self, owner, row, col):
        super().__init__(owner, row, col)
    def get_char(self) -> str:
        if self.owner.is_white:
            return "♚"
        else:
            return "♔"
    def get_possible_movements(self):
        return [(4, 4)]
    
    def get_possible_kills(self):
        return [(5, 5)]