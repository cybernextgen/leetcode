import unittest
from typing import List

data = (([2, 1, 3], 2), ([3, 2, 1, 4], 2), ([1, 2], -1), ([3, 30, 24], 24))


class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1

        result = -1
        min_num = None
        max_num = None

        for num in nums:
            if not min_num:
                min_num = num
                continue

            if not max_num:
                max_num = max(min_num, num)
                min_num = min(min_num, num)
                continue

            if num < min_num:
                return min_num
            elif num > max_num:
                return max_num
            elif num != min_num and num != max_num:
                return num
        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for nums, expected in data:
            self.assertEqual(expected, s.findNonMinOrMax(nums))


if __name__ == "__main__":
    unittest.main()
