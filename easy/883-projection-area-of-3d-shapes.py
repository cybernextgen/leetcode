import unittest
from typing import List

data = (([[1, 2], [3, 4]], 17), ([[2]], 5), ([[1, 0], [0, 2]], 8))


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        max_rows_values = [0] * len(grid)
        max_cols_values = [0] * len(grid[0])
        base_area = 0
        for row_index, row in enumerate(grid):
            max_rows_values[row_index] = max(row)
            for col_index, col in enumerate(row):
                max_cols_values[col_index] = max(max_cols_values[col_index], col)
                if col:
                    base_area += 1
        return sum(max_rows_values) + sum(max_cols_values) + base_area


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for grid, expected in data:
            self.assertEqual(expected, s.projectionArea(grid))


if __name__ == "__main__":
    unittest.main()
