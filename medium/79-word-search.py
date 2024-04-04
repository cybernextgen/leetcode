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
        for row_index, row in enumerate(board):
            for col_index, ch in enumerate(row):
                if ch != word[0]:
                    continue
                visited = set()
                visited.add(self.__get_cell_id(board, row_index, col_index))
                if self.__exist(board, word[1:], row_index, col_index, visited):
                    return True
        return False

    def __exist(
        self,
        board: List[List[str]],
        word: str,
        row_index: int,
        col_index: int,
        visited: Set[int],
    ) -> bool:
        if not word:
            return True
        current_id = self.__get_cell_id(board, row_index, col_index)
        for next_row_index, next_col_index in [
            [row_index, col_index + 1],
            [row_index, col_index - 1],
            [row_index + 1, col_index],
            [row_index - 1, col_index],
        ]:
            if (
                self.__get_char(board, next_row_index, next_col_index) != word[0]
                or self.__get_cell_id(board, next_row_index, next_col_index) in visited
            ):
                continue

            next_visited = set(visited)
            next_visited.add(self.__get_cell_id(board, next_row_index, next_col_index))
            if self.__exist(
                board,
                word[1:],
                next_row_index,
                next_col_index,
                next_visited,
            ):
                return True
        return False

    def __get_cell_id(
        self, board: List[List[str]], row_index: int, col_index: int
    ) -> int:
        return row_index * len(board[0]) + col_index

    def __get_char(
        self,
        board: List[List[str]],
        row_index: int,
        col_index: int,
    ) -> Optional[str]:
        if (
            row_index >= len(board)
            or row_index < 0
            or col_index >= len(board[0])
            or col_index < 0
        ):
            return

        return board[row_index][col_index]


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for board, word, expected in data:
            self.assertEqual(expected, s.exist(board, word))


if __name__ == "__main__":
    unittest.main()
