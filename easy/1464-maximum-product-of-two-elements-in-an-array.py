import unittest
from typing import List

data = (([3, 4, 5, 2], 12), ([1, 5, 4, 5], 16))


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        m1 = sorted_nums.pop()
        m2 = sorted_nums.pop()
        return (m1 - 1) * (m2 - 1)


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(s.maxProduct(input_data), expected)


if __name__ == "__main__":
    unittest.main()
