import unittest
from typing import List
import functools

data = (([1, 2, 3, 4], 21), ([2, 7, 1, 19, 18, 3], 63))


class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        filtered = [
            element
            for index, element in enumerate(nums)
            if len(nums) % (index + 1) == 0
        ]
        return functools.reduce(lambda x, y: x + y * y, filtered, 0)


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for nums, expected in data:
            self.assertEqual(s.sumOfSquares(nums), expected)


if __name__ == "__main__":
    unittest.main()
