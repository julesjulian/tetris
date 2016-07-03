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
    board.insert_new_piece(new_piece=piece, x_pos=x_pos)
    board.draw()


@pytest.mark.parametrize('x_pos', (-1, -10, 23, 66))
def test_piece_cannot_be_inserted_at_invalid_position(board, piece, x_pos):
    with pytest.raises(Exception):
        board.insert_new_piece(new_piece=piece, x_pos=x_pos)


@pytest.mark.parametrize('x_pos', (5, 15))
def test_piece_cannot_be_inserted_where_there_already_is_one(board, piece, x_pos):
    board.insert_new_piece(new_piece=piece, x_pos=x_pos)
    with pytest.raises(ValueError):
        board.insert_new_piece(new_piece=piece, x_pos=x_pos)


def test_pieces_are_properly_dropped(board):
    new_piece = Piece(x=7, y=0)
    board.insert_new_piece(new_piece=new_piece, x_pos=new_piece.x)
    board.drop_piece()
    assert new_piece.y == 1


def test_pieces_can_be_moved_left(board):
    new_piece = Piece(x=7, y=0)
    board.insert_new_piece(new_piece=new_piece, x_pos=new_piece.x)
    board.move_left()
    assert new_piece.x == 6


def test_pieces_can_be_moved_right(board):
    new_piece = Piece(x=7, y=0)
    board.insert_new_piece(new_piece=new_piece, x_pos=new_piece.x)
    board.move_right()
    assert new_piece.x == 8


def test_pieces_cannot_be_moved_beyond_the_left_edge(board):
    new_piece = Piece(x=0, y=0)
    assert new_piece.x == 0
    board.insert_new_piece(new_piece=new_piece, x_pos=new_piece.x)
    board.move_left()
    assert new_piece.x == 0


@pytest.mark.parametrize('shape,shape_width', ((0, 1), (1, 2), (2, 2), (3, 2), (4, 2)))
def test_pieces_cannot_be_moved_beyond_the_right_edge(board, shape, shape_width):
    new_piece = Piece(x=16, y=0, shape=shape) # board width = 20
    assert new_piece.x == 16
    board.insert_new_piece(new_piece=new_piece, x_pos=new_piece.x)
    for unused in range(10):
        board.move_right()
    assert new_piece.x == 20 - shape_width


def test_clockwise_rotation_possible(board):
    new_piece = Piece(x=7, y=0)
    board.insert_new_piece(new_piece=new_piece, x_pos=new_piece.x)
    board.rotate_clockwise()


def test_counterclockwise_rotation_possible(board):
    new_piece = Piece(x=7, y=0)
    board.insert_new_piece(new_piece=new_piece, x_pos=new_piece.x)
    board.rotate_counterclockwise()
