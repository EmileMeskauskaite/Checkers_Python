import unittest
from unittest.mock import patch
from CheckersBoard import CheckersBoard, BROWN, BLUE

class TestValidMove(unittest.TestCase):
    def setUp(self):
        self.board = CheckersBoard()

    def test_valid_move(self):

        piece = self.board.get_piece_at(2, 1)
        piece.color = BROWN

        self.assertTrue(self.board.is_valid_move(piece, 3, 2))
        self.assertFalse(self.board.is_valid_move(piece, 2, 0))
        self.assertFalse(self.board.is_valid_move(piece, 1, 0))
        self.assertFalse(self.board.is_valid_move(piece, 3, 1))


if __name__ == "__main__":
    unittest.main()
