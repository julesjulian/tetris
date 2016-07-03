from tetris.main import Board


def test_initialization():
    Board()


def test_board_can_be_drawn():
    board = Board()
    board.draw()
