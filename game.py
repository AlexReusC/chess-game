from board import Board
from player import Player

class Game():
    def __init__(self):
        self.board = Board()
        self.white_player = Player()
        self.black_player = Player()
        self.is_white_turn = True



