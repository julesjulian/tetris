#!/usr/bin/env python3
import os

from tetris.board import Board
from tetris.piece import Piece


def _new_piece():
    board.insert_new_piece(new_piece=Piece())
    board.draw()
    while True:
        input('Enter command (w, a, s, d): ')
        if board.can_drop():
            board.drop_piece()
            board.draw()
        else:
            return


if __name__ == '__main__':
    os.system('clear')
    board = Board(pieces=[])
    _new_piece()
    _new_piece()
