from tetris.main import Board, Piece


def test_board_initialization():
    Board()


def test_board_can_be_drawn():
    board = Board()
    board.draw()


def test_piece_initialization():
    Piece()


def test_piece_can_be_drawn():
    piece = Piece()
    piece.draw()
