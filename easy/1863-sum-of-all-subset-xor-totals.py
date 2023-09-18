import unittest
from typing import List
import itertools
import functools

data = (([1, 3], 6), ([5, 1, 6], 28), ([3, 4, 5, 6, 7, 8], 480))


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result = sum(nums)
        for subset_len in range(2, len(nums) + 1):
            for combination in itertools.combinations(nums, subset_len):
                result += functools.reduce(lambda x, y: x ^ y, combination, 0)
        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for nums, expected in data:
            self.assertEqual(expected, s.subsetXORSum(nums))


if __name__ == "__main__":
    unittest.main()
