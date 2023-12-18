import unittest

from CheckerPiece import CheckerPiece
from CheckersGame import CheckersGame
from main import BROWN


class TestPieceMoveOutOfBounds(unittest.TestCase):
    def setUp(self):
        self.game = CheckersGame()
        self.board = self.game.board

    def test_piece_move_out_of_bounds(self):
        initial_position = (0, 0)
        piece = CheckerPiece(self.board.screen, BROWN, *initial_position)
        self.board.pieces.append(piece)

        self.board.handle_click(initial_position)

        target_position = (-1, -1)
        self.board.handle_click(target_position)

        self.assertIsNotNone(piece)

        self.assertEqual((piece.row, piece.col), initial_position)

if __name__ == "__main__":
    unittest.main()
