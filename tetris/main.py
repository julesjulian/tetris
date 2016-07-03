#!/usr/bin/env python3
import os
import random

import numpy as np


MATTER = '*'
VOID = ' '


class Board():
    """
    The board that the Tetris game is played on.

    The board has a fixed height and width of 20 grid boxes, and a frame around it is displayed on
    all sides except for the top, where pieces can enter.
    """

    _WIDTH = 20
    _HEIGHT = 20

    def __init__(self):
        self._playing_field = np.array([[False] * self._WIDTH] * self._HEIGHT)

    def draw(self):
        for line in self._playing_field:
            print(MATTER, end='') # left edge
            for column in line:
                print(MATTER if column else VOID, end='')
            print(MATTER) # right edge
        print(MATTER * (self._WIDTH + 2)) # bottom


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

    def __init__(self):
        self._shape = self._SHAPES[random.randint(0, len(self._SHAPES) - 1)]

    def draw(self):
        for line in self._shape:
            for column in line:
                print(MATTER if column else VOID, end='')
            print('')


def _initialize_game():
    os.system('clear')
    board = Board()
    board.draw()

if __name__ == '__main__':
    _initialize_game()
