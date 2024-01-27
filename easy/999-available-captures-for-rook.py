import unittest
from typing import List

data = (
    (
        [
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "p", ".", ".", ".", "."],
            [".", ".", ".", "R", ".", ".", ".", "p"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "p", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
        ],
        3,
    ),
    (
        [
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", "p", "p", "p", "p", "p", ".", "."],
            [".", "p", "p", "B", "p", "p", ".", "."],
            [".", "p", "B", "R", "B", "p", ".", "."],
            [".", "p", "p", "B", "p", "p", ".", "."],
            [".", "p", "p", "p", "p", "p", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
        ],
        0,
    ),
    (
        [
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "p", ".", ".", ".", "."],
            [".", ".", ".", "p", ".", ".", ".", "."],
            ["p", "p", ".", "R", ".", "p", "B", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "B", ".", ".", ".", "."],
            [".", ".", ".", "p", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
        ],
        3,
    ),
)


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        rook_row_index = 0
        rook_col_index = 0
        for row_index, row in enumerate(board):
            for col_index, col in enumerate(row):
                if board[row_index][col_index] == "R":
                    rook_row_index = row_index
                    rook_col_index = col_index
                    break
            else:
                continue
            break

        result = 0
        for drow, dcol in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            current_row = rook_row_index + drow
            current_col = rook_col_index + dcol
            while 0 <= current_row < 8 and 0 <= current_col < 8:
                cell_value = board[current_row][current_col]
                if cell_value == "B":
                    break
                if cell_value == "p":
                    result += 1
                    break
                current_col += dcol
                current_row += drow

        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for board, expected in data:
            self.assertEqual(s.numRookCaptures(board), expected)


if __name__ == "__main__":
    unittest.main()
