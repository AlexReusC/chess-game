import sys
import curses

from board import Board
from player import Player
from piece import Pawn

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

        self.board.add_piece(Pawn(self.white_player, 0, 0))



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
            case _:
                return "*"



