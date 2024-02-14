import unittest
from typing import List

data = (([1, 7, 3, 6, 5, 6], 3), ([1, 2, 3], -1), ([2, 1, -1], 0))


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right_sum = sum(nums)
        left_sum = 0
        for index, num in enumerate(nums):
            right_sum -= num
            if left_sum == right_sum:
                return index
            left_sum += num
        return -1


class Test(unittest.TestCase):
    def test_parse(self):
        s = Solution()

        for nums, expected in data:
            self.assertEqual(s.pivotIndex(nums), expected)


if __name__ == "__main__":
    unittest.main()
