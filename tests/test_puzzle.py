import unittest
import os
import sys

# Add the puzzle directory to sys.path
TEST_DIR = os.path.dirname(__file__)
PUZZLE_DIR = os.path.abspath(os.path.join(TEST_DIR, '..', 'ejercicios', 'puzzle'))
sys.path.insert(0, PUZZLE_DIR)

from challenge import Puzzle

class TestPuzzleResolvability(unittest.TestCase):
    def test_solvable_puzzle(self):
        board = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        puzzle = Puzzle(board)
        self.assertTrue(puzzle.es_resoluble())

    def test_unsolvable_puzzle(self):
        board = [[1, 2, 3], [4, 5, 6], [8, 7, 0]]
        puzzle = Puzzle(board)
        self.assertFalse(puzzle.es_resoluble())

if __name__ == "__main__":
    unittest.main()
