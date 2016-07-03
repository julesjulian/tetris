#!/usr/bin/env python3
import os

from tetris.board import Board


def _initialize_game():
    os.system('clear')
    board = Board()
    board.draw()

if __name__ == '__main__':
    _initialize_game()
