import unittest
from typing import List

data = (([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]], 16), ([[1, 0]], 4))


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        for row_index, row in enumerate(grid):
            for col_index, cell in enumerate(row):
                if not cell:
                    continue
                perimeter += [
                    self.__cell_is_land(grid, col_index, row_index - 1),
                    self.__cell_is_land(grid, col_index, row_index + 1),
                    self.__cell_is_land(grid, col_index - 1, row_index),
                    self.__cell_is_land(grid, col_index + 1, row_index),
                ].count(False)
        return perimeter

    @staticmethod
    def __cell_is_land(grid: List[List[int]], col: int, row: int) -> bool:
        if col < 0 or row < 0:
            return False

        try:
            return grid[row][col] == 1
        except IndexError:
            return False


class Test(unittest.TestCase):
    def test_parse(self):
        s = Solution()

        for grid, expected in data:
            self.assertEqual(s.islandPerimeter(grid), expected)


if __name__ == "__main__":
    unittest.main()
