import unittest
from typing import List

data = (([[0, 1], [0, 0]], 0), ([[0, 0, 1], [1, 0, 1], [0, 0, 0]], 1))


class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        for index, row in enumerate(grid):
            if sum(row) == len(row) - 1:
                return index
        return 0


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for grid, expected in data:
            self.assertEqual(expected, s.findChampion(grid))


if __name__ == "__main__":
    unittest.main()
