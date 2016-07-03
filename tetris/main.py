#!/usr/bin/env python3
import os

from tetris.board import Board
from tetris.piece import Piece


if __name__ == '__main__':
    os.system('clear')
    board = Board()
    board.draw()
    board.insert_new_piece(piece=Piece())
    board.draw()
    board.drop_pieces()
    board.draw()
