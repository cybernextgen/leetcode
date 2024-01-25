import unittest
from typing import List

data = (([1, 3, 5, 4, 2, 3, 4, 5], 4), ([1, 3, 5, 4, 7], 3), ([2, 2, 2, 2, 2], 1))


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        max_length = 1
        current_length = 1
        prev_num = nums[0]
        for num in nums[1:]:
            if num > prev_num:
                current_length += 1
                max_length = max(max_length, current_length)
            else:
                current_length = 1
            prev_num = num

        return max_length


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for nums, expected in data:
            self.assertEqual(s.findLengthOfLCIS(nums), expected)


if __name__ == "__main__":
    unittest.main()
