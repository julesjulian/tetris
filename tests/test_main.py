import pytest

from tetris.main import Board, Piece


@pytest.fixture
def board():
    return Board()


@pytest.fixture
def piece():
    return Piece()


def test_board_initialization():
    Board()


def test_board_can_be_drawn(board):
    board.draw()


def test_piece_initialization():
    Piece()


def test_piece_can_be_drawn(piece):
    piece.draw()


def test_piece_exposes_shape(piece):
    piece.shape


@pytest.mark.parametrize("x_pos", (1, 3, 6, 8))
def test_piece_can_be_inserted_at_valid_position(board, piece, x_pos):
    board.insert_piece(piece=piece, x_pos=x_pos)


@pytest.mark.parametrize("x_pos", (-1, -10, 23, 66))
def test_piece_cannot_be_inserted_at_invalid_position(board, piece, x_pos):
    with pytest.raises(Exception):
        board.insert_piece(piece=piece, x_pos=x_pos)
