ROWS = 8
COLS = 8

class Board():
    def __init__(self):
        self._state = [[None] * COLS for _ in range(ROWS)] 
