import unittest
from typing import List, Optional, Set

data = (
    (
        [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]],
        "ABCESEEEFS",
        True,
    ),
    ([["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]], "AAB", True),
    (
        [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        "ABCCED",
        True,
    ),
    ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE", True),
    ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB", False),
)


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        chars_stack = list(word)
        for row_index, row in enumerate(board):
            for col_index, ch in enumerate(row):
                if ch != chars_stack[-1]:
                    continue
                if self.__exist(board, chars_stack, row_index, col_index):
                    return True
        return False

    def __exist(
        self,
        board: List[List[str]],
        chars_stack: List[str],
        row_index: int,
        col_index: int,
    ) -> bool:
        last_ch = chars_stack.pop()

        if not chars_stack:
            return True

        last_board_ch = board[row_index][col_index]
        board[row_index][col_index] = "#"

        for next_row_index, next_col_index in [
            [row_index, col_index + 1],
            [row_index, col_index - 1],
            [row_index + 1, col_index],
            [row_index - 1, col_index],
        ]:
            if (
                next_row_index >= len(board)
                or next_row_index < 0
                or next_col_index >= len(board[0])
                or next_col_index < 0
                or board[next_row_index][next_col_index] != chars_stack[-1]
            ):
                continue

            if self.__exist(board, chars_stack, next_row_index, next_col_index):
                return True

        board[row_index][col_index] = last_board_ch
        chars_stack.append(last_ch)
        return False


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for board, word, expected in data:
            self.assertEqual(expected, s.exist(board, word))


if __name__ == "__main__":
    unittest.main()
