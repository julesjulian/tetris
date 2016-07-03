import pytest
import numpy as np

from tetris.main import Board, Piece


@pytest.fixture
def board():
    return Board()


@pytest.fixture
def piece():
    return Piece(x=5, y=0, shape=3)


def test_board_initialization():
    Board()


def test_board_can_be_drawn(board):
    board.draw()


def test_piece_initialization():
    Piece(x=4, y=7, shape=2)


def test_piece_can_be_drawn(piece):
    piece.draw()


def test_piece_exposes_shape(piece):
    piece.shape == np.array(((False, True), (True, True), (True, False)))


@pytest.mark.parametrize('x_pos', (1, 3, 6, 8))
def test_piece_can_be_inserted_at_valid_position(board, piece, x_pos):
    board.insert_new_piece(piece=piece, x_pos=x_pos)
    board.draw()


@pytest.mark.parametrize('x_pos', (-1, -10, 23, 66))
def test_piece_cannot_be_inserted_at_invalid_position(board, piece, x_pos):
    with pytest.raises(Exception):
        board.insert_new_piece(piece=piece, x_pos=x_pos)


@pytest.mark.parametrize('x_pos', (1, 3, 6, 8))
def test_piece_exposes_x_coordinate(x_pos):
    piece = Piece(x=x_pos, y=0)
    assert piece.x == x_pos


@pytest.mark.parametrize('y_pos', (1, 3, 6, 8))
def test_piece_exposes_y_coordinate(y_pos):
    piece = Piece(x=10, y=y_pos)
    assert piece.y == y_pos


@pytest.mark.parametrize('x_pos', (5, 15))
def test_piece_cannot_be_inserted_where_there_already_is_one(board, piece, x_pos):
    board.insert_new_piece(piece=piece, x_pos=x_pos)
    with pytest.raises(ValueError):
        board.insert_new_piece(piece=piece, x_pos=x_pos)
