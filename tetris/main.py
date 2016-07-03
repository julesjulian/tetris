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
        self._clear()
        self._pieces = []

    def draw(self):
        for piece in self._pieces:
            self._insert_piece(piece=piece, x_pos=piece.x, y_pos=piece.y)
        print('\n') # start in new line
        for row in self._playing_field:
            print(MATTER, end='') # left edge
            for column in row:
                print(MATTER if column else VOID, end='')
            print(MATTER) # right edge
        print(MATTER * (self._WIDTH + 2)) # bottom

    def insert_new_piece(self, piece, x_pos):
        """Insert a piece at a specified x-position in the first row."""
        self._clear()
        for piece in self._pieces:
            self._insert_piece(piece=piece, x_pos=piece.x, y_pos=piece.y)
        self._check_validity(piece=piece, x_pos=x_pos, y_pos=0)
        piece.x = x_pos
        piece.y = 0
        self._pieces.append(piece)

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
        for row in self._shape:
            for column in row:
                print(MATTER if column else VOID, end='')
            print('')


def _initialize_game():
    os.system('clear')
    board = Board()
    board.draw()

if __name__ == '__main__':
    _initialize_game()
