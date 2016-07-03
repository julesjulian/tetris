import random

import numpy as np


class Piece():
    """
    A Tetris piece.

    The piece can have one of five shapes: Stick, L-shaped, inverse-L, inverse-S, or a Block.

    Parameters:
    * x: The position on the x-axis.
    * y: The position on the y-axis.
    * shape: An integer between 0 and 4 for one of the above-mentioned shapes (default: random).
    """

    _SHAPES = (
        np.array(((True,), (True,), (True,), (True,))), # Stick
        np.array(((True, False), (True, False), (True, True))), # L
        np.array(((False, True), (False, True), (True, True))), # Inverse L
        np.array(((False, True), (True, True), (True, False))), # Inverse S
        np.array(((True, True), (True, True))) # Block
    )

    def __init__(self, x=None, y=None, shape='Random'):
        if shape == 'Random':
            self._shape = self._SHAPES[random.randint(0, len(self._SHAPES) - 1)]
        else:
            self._shape = self._SHAPES[shape]
        self.x = x
        self.y = y

    @property
    def shape(self):
        """The shape of the piece, a numpy array."""
        return self._shape

    def rotate_clockwise(self):
        """Rotate the piece 90 degrees clockwise."""
        for unused in range(3):
            self._shape = np.rot90(self._shape)

    def rotate_counterclockwise(self):
        """Rotate the piece 90 degrees counterclockwise."""
        self._shape = np.rot90(self._shape)
