#!/usr/bin/env python3
import os

from tetris.board import Board
from tetris.piece import Piece

GAME_OVER_MESSAGE = """
#####################
# G A M E   O V E R #
#####################
"""


def _new_piece(board):
    try:
        board.insert_new_piece(new_piece=Piece())
    except ValueError:
        print(GAME_OVER_MESSAGE)
        raise
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


def run_from_command_line():
    os.system('clear')
    board = Board(pieces=[])
    while True:
        try:
            _new_piece(board)
        except ValueError:
            break

if __name__ == '__main__':
    run_from_command_line()
