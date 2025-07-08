class Piece():
    def __init__(self, owner, row, col):
        self.owner = owner
        self.row = row
        self.col = col


class Pawn(Piece):
    def __init__(self, owner, row, col):
        super().__init__(owner, row, col)
"""
class Rook(Piece):

class Knight(Piece):

class Bishop(Piece):

class Queen(Piece):

class King(Piece):
"""