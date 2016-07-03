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

    def __init__(self, pieces):
        self._pieces = pieces
        self._clear()

    def draw(self):
        """Print the current situation to the screen."""
        self._clear()
        for piece in self._pieces:
            self._insert_piece(piece=piece, x_pos=piece.x, y_pos=piece.y)
        print('\n') # start in new line
        for row in self._playing_field:
            print(self._MATTER, end='') # left edge
            for column in row:
                print(self._MATTER if column else self._VOID, end='')
            print(self._MATTER) # right edge
        print(self._MATTER * (self._WIDTH + 2)) # bottom

    def insert_new_piece(self, new_piece, x_pos=None):
        """
        Insert a piece at a specified x-position in the first row.

        Parameters:
        * new_piece: the piece
        * x_pos: the position on the x-axis where the piece should be positioned
        """
        self._clear()
        for piece in self._pieces:
            self._insert_piece(piece=piece, x_pos=piece.x, y_pos=piece.y)
        if x_pos is None:
            x_pos = round(self._WIDTH / 2 - 1)
        self._check_validity(piece=new_piece, x_pos=x_pos, y_pos=0)
        new_piece.x = x_pos
        new_piece.y = 0
        self._pieces.append(new_piece)

    def drop_piece(self):
        """Drop last piece by 1 field."""
        self._pieces[-1].y += 1

    def can_drop(self):
        """Whether dropping the last piece by one field is possible in the current situation."""
        self._clear()
        for piece in self._pieces[:-1]:
            self._insert_piece(piece, x_pos=piece.x, y_pos=piece.y)
        try:
            self._check_validity(self._pieces[-1], x_pos=self._pieces[-1].x, y_pos=self._pieces[-1].y + 1)
            self._insert_piece(self._pieces[-1], x_pos=self._pieces[-1].x, y_pos=self._pieces[-1].y + 1)
        except (IndexError, ValueError):
            return False
        return True

    def rotate_clockwise(self):
        """Rotate the last piece clockwise."""
        self._pieces[-1].rotate_clockwise()

    def rotate_counterclockwise(self):
        """Rotate the last piece counterclockwise."""
        self._pieces[-1].rotate_counterclockwise()

    def move_left(self):
        """Move the last piece to the left."""
        if self._can_move_horizontally(move=-1):
            self._pieces[-1].x -= 1

    def move_right(self):
        """Move the last piece to the right."""
        if self._can_move_horizontally(move=+1):
            self._pieces[-1].x += 1

    def _can_move_horizontally(self, move):
        self._clear()
        for piece in self._pieces[:-1]:
            self._insert_piece(piece, x_pos=piece.x, y_pos=piece.y)
        try:
            self._check_validity(self._pieces[-1],
                                 x_pos=self._pieces[-1].x + move,
                                 y_pos=self._pieces[-1].y)
            self._insert_piece(self._pieces[-1],
                               x_pos=self._pieces[-1].x + move,
                               y_pos=self._pieces[-1].y)
        except (IndexError, ValueError):
            return False
        return True

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
