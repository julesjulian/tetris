#!/usr/bin/env python3
import os


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


def _initialize_game():
    os.system('clear')
    board = Board()
    board.draw()

if __name__ == '__main__':
    _initialize_game()
