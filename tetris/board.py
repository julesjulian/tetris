import numpy as np


class Board():
    """
    The board that the Tetris game is played on.

    The board has a fixed height and width of 20 grid boxes, and a frame around it is displayed on
    all sides except for the top, where pieces can enter.
    """

    _WIDTH = 20
    _HEIGHT = 20
    _MATTER = '*'
    _VOID = ' '

    def __init__(self, pieces=[]):
        self._clear()
        self._pieces = pieces

    def draw(self):
        for piece in self._pieces:
            self._insert_piece(piece=piece, x_pos=piece.x, y_pos=piece.y)
        print('\n') # start in new line
        for row in self._playing_field:
            print(self._MATTER, end='') # left edge
            for column in row:
                print(self._MATTER if column else self._VOID, end='')
            print(self._MATTER) # right edge
        print(self._MATTER * (self._WIDTH + 2)) # bottom

    def insert_new_piece(self, piece, x_pos=None):
        """Insert a piece at a specified x-position in the first row."""
        self._clear()
        for piece in self._pieces:
            self._insert_piece(piece=piece, x_pos=piece.x, y_pos=piece.y)
        if x_pos is None:
            x_pos = round(self._WIDTH / 2 - 1)
        self._check_validity(piece=piece, x_pos=x_pos, y_pos=0)
        piece.x = x_pos
        piece.y = 0
        self._pieces.append(piece)

    def drop_pieces(self):
        """Drop all pieces by 1 field."""
        for piece in self._pieces:
            piece.y -= 1

    def _insert_piece(self, piece, x_pos, y_pos):
        for row in range(len(piece.shape)):
            for column in range(len(piece.shape[row])):
                if piece.shape[row, column]:
                    self._playing_field[row + y_pos, column + x_pos] = True

    def _check_validity(self, piece, x_pos, y_pos):
        if x_pos < 0:
            raise IndexError('Can only insert pieces at positive indices, but received {}.'
                             .format(x_pos))
        for row in range(len(piece.shape)):
            for column in range(len(piece.shape[row])):
                if piece.shape[row, column] and self._playing_field[row + y_pos, column + x_pos]:
                    raise ValueError('Pieces overlapping.')

    def _clear(self):
        self._playing_field = np.array([[False] * self._WIDTH] * self._HEIGHT)
