import unittest
from math import sqrt, ceil
from typing import List

data = (([2, 5, 6, 9, 10], 2), ([7, 5, 6, 8, 3], 1), ([3, 3], 3))


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_num = min(nums)
        max_num = max(nums)
        return min_num * max_num // self.find_lcm(min_num, max_num)

    def find_lcm(self, num1: int, num2: int) -> int:
        if num1 > num2:
            num1, num2 = num2, num1

        step = 1
        while True:
            multiplier = num2 * step
            if multiplier % num1 == 0:
                return multiplier
            step += 1


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for nums, expected in data:
            self.assertEqual(expected, s.findGCD(nums))


if __name__ == "__main__":
    unittest.main()
