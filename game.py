import sys
import curses
import typing

from board import Board
from player import Player
from piece import Piece, Pawn, Rook, Knight, Bishop, King, Queen


class Game():
    def __init__(self):
        self.board = Board()
        self.white_player = Player(True)
        self.black_player = Player(False)
        self.current_player : Player = self.white_player
        self.cursor_y, self.cursor_x = 0, 0
        self.is_piece_selected = False
        self.selected_piece : typing.Optional[Piece] = None
        self.possible_movements = []
        self.possible_kills = []

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
        while True:
            curses.start_color()
            curses.use_default_colors()
            curses.init_pair(1, curses.COLOR_WHITE, -1)  
            curses.init_pair(2, curses.COLOR_BLUE, -1)  
            curses.init_pair(3, curses.COLOR_GREEN, -1)
            curses.init_pair(4, curses.COLOR_RED, -1)

            if not self.is_piece_selected:
                self.possible_movements = self.board.get_possible_movements(self.cursor_y, self.cursor_x) 
                self.possible_kills = self.board.get_possible_kills(self.cursor_y, self.cursor_x)

            self.render(stdscr)
            if self.process_keys(stdscr):
                break
            

    def render(self, stdscr):
        stdscr.clear()
        for row in range(8):
            for col in range(8):

                char = self.get_char(row, col)
                color = curses.color_pair(1)
                if (row, col) in self.possible_movements:
                    color = curses.color_pair(3)
                elif (row, col) in self.possible_kills:
                    color = curses.color_pair(4)
                elif row == self.cursor_y and col == self.cursor_x:
                    color = curses.color_pair(2)

                try:
                    stdscr.addstr(row, col * 2, f"{char} ", color)
                except curses.error:
                    pass

        stdscr.addstr(9, 0, "White player turn ", curses.color_pair(1))

        stdscr.refresh()

    def process_keys(self, stdscr): 
        key = stdscr.getch()
        if key == curses.KEY_UP:
            self.cursor_y = max(self.cursor_y - 1, 0)
        elif key == curses.KEY_DOWN:
            self.cursor_y = min(self.cursor_y + 1, 7)
        elif key == curses.KEY_RIGHT:
            self.cursor_x = min(self.cursor_x + 1, 7)
        elif key == curses.KEY_LEFT:
            self.cursor_x = max(self.cursor_x - 1, 0)
        elif key == ord(' '):
            if self.is_piece_selected:
                self.move_piece()
            elif self.board.get_piece_at_position(self.cursor_y, self.cursor_x):
                self.select_piece()
        elif key == ord('q'):
            return True
        
        return False

    def change_player(self):
        pass

    def select_piece(self):
        piece = self.board.get_piece_at_position(self.cursor_y, self.cursor_x)
        if not piece or piece.owner != self.current_player :
            return

        self.selected_piece = piece
        self.is_piece_selected = True

    def move_piece(self):
        if (self.cursor_y, self.cursor_x) in self.possible_movements or (self.cursor_y, self.cursor_x) in self.possible_kills:
            self.board.move_piece(self.selected_piece.row, self.selected_piece.col, self.cursor_y, self.cursor_x)
            self.is_piece_selected = False
            self.change_player()


    def get_char(self, row, col):
        piece : Piece = self.board.get_piece_at_position(row, col)
        if piece:
            return piece.get_char()
        return "*"
    

     


