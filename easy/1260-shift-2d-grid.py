import unittest
from typing import List

data = (
    ([[1], [2], [3], [4], [7], [6], [5]], 23, [[6], [5], [1], [2], [3], [4], [7]]),
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, [[9, 1, 2], [3, 4, 5], [6, 7, 8]]),
    (
        [[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]],
        4,
        [[12, 0, 21, 13], [3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10]],
    ),
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 9, [[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
)


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        if not grid:
            return [[]]

        rows_count = len(grid)
        cols_count = len(grid[0])

        k = k % (rows_count * cols_count)

        grid_as_list = [e for row in grid for e in row]
        grid_as_list = grid_as_list[-k:] + grid_as_list[:-k]

        for row_index in range(rows_count):
            for col_index in range(cols_count):
                grid[row_index][col_index] = grid_as_list[
                    row_index * cols_count + col_index
                ]
        return grid


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for grid, k, expected in data:
            self.assertListEqual(expected, s.shiftGrid(grid, k))


if __name__ == "__main__":
    unittest.main()
