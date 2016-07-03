import random

import numpy as np


class Piece():
    """
    A Tetris piece.

    The piece can have one of five shapes.
    """

    _SHAPES = (
        np.array(((True,), (True,), (True,), (True,))), # Stick
        np.array(((True, False), (True, False), (True, True))), # L
        np.array(((False, True), (False, True), (True, True))), # Inverse L
        np.array(((False, True), (True, True), (True, False))), # Inverse S
        np.array(((True, True), (True, True))) # Block
    )

    def __init__(self, x, y, shape='Random'):
        if shape == 'Random':
            self._shape = self._SHAPES[random.randint(0, len(self._SHAPES) - 1)]
        else:
            self._shape = self._SHAPES[shape]
        self.x = x
        self.y = y

    @property
    def shape(self):
        return self._shape

    def draw(self):
        MATTER = '*'
        VOID = ' '
        for row in self._shape:
            for column in row:
                print(MATTER if column else VOID, end='')
            print('')
