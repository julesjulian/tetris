import numpy as np
import pytest

from tetris.piece import Piece


@pytest.fixture
def piece():
    return Piece(x=5, y=0, shape=3)


def test_piece_initialization():
    Piece(x=4, y=7, shape=2)


def test_piece_exposes_shape(piece):
    np.testing.assert_array_equal(
        piece.shape,
        np.array(((False, True), (True, True), (True, False)))
    )


@pytest.mark.parametrize('x_pos', (1, 3, 6, 8))
def test_piece_exposes_x_coordinate(x_pos):
    piece = Piece(x=x_pos, y=0)
    assert piece.x == x_pos


@pytest.mark.parametrize('y_pos', (1, 3, 6, 8))
def test_piece_exposes_y_coordinate(y_pos):
    piece = Piece(x=10, y=y_pos)
    assert piece.y == y_pos
