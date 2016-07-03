import pytest

from tetris.board import Board


@pytest.fixture
def board():
    return Board()


def test_board_initialization():
    Board()


def test_board_can_be_drawn(board):
    board.draw()
