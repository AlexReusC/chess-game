import sys
import curses

from board import Board
from player import Player
from piece import Pawn, Rook, Knight, Bishop, King, Queen

board = [
    ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜'],
    ['♟'] * 8,
    ['*'] * 8,
    ['*'] * 8,
    ['*'] * 8,
    ['*'] * 8,
    ['♙'] * 8,
    ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖']
]

class Game():
    def __init__(self):
        self.board = Board()
        self.white_player = Player(True)
        self.black_player = Player(False)
        self.is_white_turn = True

        for col in range(8):
            self.board.add_piece(Pawn(self.white_player, 1, col))
        self.board.add_piece(Rook(self.white_player, 0, 0))
        self.board.add_piece(Knight(self.white_player, 0, 1))
        self.board.add_piece(Bishop(self.white_player, 0, 2))
        self.board.add_piece(Queen(self.white_player, 0, 3))
        self.board.add_piece(King(self.white_player, 0, 4))
        self.board.add_piece(Bishop(self.white_player, 0, 5))
        self.board.add_piece(Knight(self.white_player, 0, 6))
        self.board.add_piece(Rook(self.white_player, 0, 7))

        for col in range(8):
            self.board.add_piece(Pawn(self.black_player, 6, col))
        self.board.add_piece(Rook(self.black_player, 7, 0))
        self.board.add_piece(Knight(self.black_player, 7, 1))
        self.board.add_piece(Bishop(self.black_player, 7, 2))
        self.board.add_piece(Queen(self.black_player, 7, 3))
        self.board.add_piece(King(self.black_player, 7, 4))
        self.board.add_piece(Bishop(self.black_player, 7, 5))
        self.board.add_piece(Knight(self.black_player, 7, 6))
        self.board.add_piece(Rook(self.black_player, 7, 7))



    def run(self, stdscr):
        curses.start_color()
        curses.use_default_colors()
        curses.init_pair(1, curses.COLOR_WHITE, -1)  


        stdscr.clear()
        for y in range(8):
            for x in range(8):


                char = self.get_char(y, x)
                color = curses.color_pair(1)

                try:
                    stdscr.addstr(y, x * 2, f"{char} ", color)
                except curses.error:
                    pass

        stdscr.refresh()
        stdscr.getch()


    def get_char(self, y, x):
        match self.board.get_piece_at_position(y, x):
            case None:
                return "*"
            case (Pawn(), True):
                return "♟"
            case (Pawn(), False):
                return "♙"
            case (Rook(), True):
                return "♜"
            case (Rook(), False):
                return "♖"
            case (Knight(), True):
                return "♞"
            case (Knight(), False):
                return "♘"
            case (Bishop(), True):
                return "♝"
            case (Bishop(), False):
                return "♗"
            case (Queen(), True):
                return "♛"
            case (Queen(), False):
                return "♕"
            case (King(), True):
                return "♚"
            case (King(), False):
                return "♔"
            case _:
                return "*"



