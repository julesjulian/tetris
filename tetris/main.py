#!/usr/bin/env python3
import os
import random


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

    def draw(self):
        for line in range(self._HEIGHT):
            print(MATTER + VOID * self._WIDTH + MATTER)
        print(MATTER * (self._WIDTH + 2))


class Piece():
    """
    A Tetris piece.

    The piece can have one of five shapes.
    """

    _SHAPES = (
        ((True,), (True,), (True,), (True,)), # Stick
        ((True, False), (True, False), (True, True)), # L
        ((False, True), (False, True), (True, True)), # Inverse L
        ((False, True), (True, True), (True, False)), # Inverse S
        ((True, True), (True, True)) # Block
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
