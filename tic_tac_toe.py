import unittest

from tic_tac_toe import check_winner, is_draw, is_valid_move


class TicTacToeTests(unittest.TestCase):
    def test_winner_detects_row(self):
        board = ["X", "X", "X", "O", "O", " ", " ", " ", " "]
        self.assertEqual(check_winner(board), "X")

    def test_winner_detects_diagonal(self):
        board = ["O", "X", "X", "X", "O", " ", " ", " ", "O"]
        self.assertEqual(check_winner(board), "O")

    def test_draw_detects_full_board(self):
        board = ["X", "O", "X", "X", "O", "O", "O", "X", "X"]
        self.assertTrue(is_draw(board))

    def test_valid_move_checks_empty_space(self):
        board = ["X", " ", "O", " ", "X", " ", " ", "O", " "]
        self.assertTrue(is_valid_move(board, 2))
        self.assertFalse(is_valid_move(board, 1))


if __name__ == "__main__":
    unittest.main()
