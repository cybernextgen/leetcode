import unittest
from typing import List

data = (([[9, 81], [33, 17]], 98), ([[1, 2, 4], [3, 3, 1]], 8), ([[10]], 10))


class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        result = 0
        max_element = 0
        row_index = 0

        is_grid_empty = False
        while not is_grid_empty:
            row = grid[row_index]
            m = max(row)
            max_element = max(max_element, m)
            row.remove(m)
            row_index += 1
            if row_index == len(grid):
                result += max_element
                max_element = row_index = 0
                is_grid_empty = len(row) == 0

        result += max_element
        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for grid, expected in data:
            self.assertEqual(expected, s.deleteGreatestValue(grid))


if __name__ == "__main__":
    unittest.main()
