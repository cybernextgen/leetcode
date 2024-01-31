import unittest
from typing import List

data = (
    ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], 32),
    ([[1, 2], [3, 4]], 34),
    ([[2, 2, 2], [2, 1, 2], [2, 2, 2]], 46),
)


class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        grid_len = len(grid)
        result = 0
        for row_index in range(grid_len):
            for col_index in range(grid_len):
                cell_value = grid[row_index][col_index]

                result += (cell_value * 4) + 2 if cell_value > 0 else 0
                if row_index:
                    result -= min(cell_value, grid[row_index - 1][col_index]) * 2
                if col_index:
                    result -= min(cell_value, grid[row_index][col_index - 1]) * 2
        return result


class Test(unittest.TestCase):
    def test_parse(self):
        s = Solution()

        for input_data, result in data:
            self.assertEqual(s.surfaceArea(input_data), result)


if __name__ == "__main__":
    unittest.main()
