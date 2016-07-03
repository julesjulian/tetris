import pytest

from tetris.board import Board
from tetris.piece import Piece


@pytest.fixture
def board():
    return Board(pieces=[])


@pytest.fixture
def piece():
    return Piece(x=5, y=0, shape=3)


@pytest.mark.parametrize('x_pos', (1, 3, 6, 8))
def test_piece_can_be_inserted_at_valid_position(board, piece, x_pos):
    board.insert_new_piece(piece=piece, x_pos=x_pos)
    board.draw()


@pytest.mark.parametrize('x_pos', (-1, -10, 23, 66))
def test_piece_cannot_be_inserted_at_invalid_position(board, piece, x_pos):
    with pytest.raises(Exception):
        board.insert_new_piece(piece=piece, x_pos=x_pos)


@pytest.mark.parametrize('x_pos', (5, 15))
def test_piece_cannot_be_inserted_where_there_already_is_one(board, piece, x_pos):
    board.insert_new_piece(piece=piece, x_pos=x_pos)
    with pytest.raises(ValueError):
        board.insert_new_piece(piece=piece, x_pos=x_pos)


def test_pieces_are_properly_dropped(board):
    piece = Piece(x=7, y=0)
    board.insert_new_piece(piece=piece, x_pos=piece.x)
    board.drop_pieces()
    assert piece.y == 1
