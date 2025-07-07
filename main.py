import curses
from game import Game



def main(stdscr):
    game = Game(stdscr)


   

if __name__ == "__main__":
    curses.wrapper(main)