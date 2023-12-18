import unittest
from unittest.mock import patch

from CheckerPiece import CheckerPiece
from CheckersBoard import CheckersBoard
from CheckersGame import CheckersGame
from main import BROWN, BLUE


class TestPieceCapture(unittest.TestCase):
    def setUp(self):
        self.game = CheckersGame()
        self.board = self.game.board
        self.board.pieces.append(CheckerPiece(self.board.screen, BROWN, 3, 2))

    def test_piece_capturing(self):
        piece1 = self.board.get_piece_at(3, 2)
        self.assertIsNotNone(piece1)

        piece1.color = BLUE
        piece2 = self.board.get_piece_at(2, 1)

        self.board.move_piece(piece2, 4, 3)
        piece1_after_move = self.board.get_piece_at(3, 2)
        self.assertIsNone(piece1_after_move)


if __name__ == "__main__":
    unittest.main()
