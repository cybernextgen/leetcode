import unittest
from typing import List

data = (([1, 2, 3], 1), ([2, 2, 2, 3, 3], 2))


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd_numbers_count = sum(n % 2 for n in position)
        return min(odd_numbers_count, len(position) - odd_numbers_count)


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for position, expected in data:
            self.assertEqual(s.minCostToMoveChips(position), expected)


if __name__ == "__main__":
    unittest.main()
