class Piece():
    def __init__(self, owner, row, col):
        self.owner = owner
        self.row = row
        self.col = col
        self.movements = None


class Pawn(Piece):
    def __init__(self, owner, row, col):
        super().__init__(owner, row, col)

class Rook(Piece):
    def __init__(self, owner, row, col):
        super().__init__(owner, row, col)

class Knight(Piece):
    def __init__(self, owner, row, col):
        super().__init__(owner, row, col)

class Bishop(Piece):
    def __init__(self, owner, row, col):
        super().__init__(owner, row, col)

class Queen(Piece):
    def __init__(self, owner, row, col):
        super().__init__(owner, row, col)

class King(Piece):
    def __init__(self, owner, row, col):
        super().__init__(owner, row, col)