import curses
from game import Game



def main(stdscr):
    game = Game()
    game.run(stdscr)

if __name__ == "__main__":
    curses.wrapper(main)