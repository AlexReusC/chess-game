import sys
import curses

from board import Board
from player import Player

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
    def __init__(self, stdscr):
        self.stdscr = stdscr

        self.board = Board()
        self.white_player = Player()
        self.black_player = Player()
        self.is_white_turn = True

        stdscr.clear()
        curses.start_color()
        curses.use_default_colors()
        curses.init_pair(1, curses.COLOR_WHITE, -1)  

        for y in range(8):
            for x in range(8):
                char = board[y][x]
                color = curses.color_pair(1)

                try:
                    stdscr.addstr(y, x * 2, f"{char} ", color)
                except curses.error:
                    pass

        stdscr.refresh()
        stdscr.getch()

    def run(self):
       a = 2 






