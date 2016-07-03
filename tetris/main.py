#!/usr/bin/env python3
import os

from tetris.board import Board
from tetris.piece import Piece


def _new_piece():
    board.insert_new_piece(new_piece=Piece())
    board.draw()
    while True:
        command = input('Enter command (w, a, s, d): ')
        if command == 'a':
            board.move_left()
        if command == 'd':
            board.move_right()
        if command == 's':
            board.rotate_clockwise()
        if command == 'w':
            board.rotate_counterclockwise()
        if board.can_drop():
            board.drop_piece()
            board.draw()
        else:
            return


if __name__ == '__main__':
    os.system('clear')
    board = Board(pieces=[])
    while True:
        _new_piece()
