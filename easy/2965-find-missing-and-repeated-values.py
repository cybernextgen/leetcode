import unittest
from typing import List

data = (([[1, 3], [2, 2]], [2, 4]), ([[9, 1, 7], [8, 9, 2], [3, 4, 6]], [9, 5]))


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        nums_available = set(n for n in range(1, (len(grid) ** 2) + 1))
        result = [0, 0]
        for row in grid:
            for n in row:
                if n not in nums_available:
                    result[0] = n
                else:
                    nums_available.remove(n)
        result[1] = nums_available.pop()
        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for grid, expected in data:
            self.assertEqual(expected, s.findMissingAndRepeatedValues(grid))


if __name__ == "__main__":
    unittest.main()
