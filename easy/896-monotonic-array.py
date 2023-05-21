import unittest
from typing import List

data = (([1, 2, 2, 3], True), ([6, 5, 4, 4], True), ([1, 3, 2], False))


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if not nums or len(nums) == 1:
            return True

        isIncrease = False
        isDecrease = False
        prev_num = nums[0]
        for current_num in nums[1:]:
            if current_num == prev_num:
                continue
            if current_num > prev_num:
                if isDecrease:
                    return False
                isIncrease = True
            if current_num < prev_num:
                if isIncrease:
                    return False
                isDecrease = True
            prev_num = current_num
        return True


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(s.isMonotonic(input_data), expected)


if __name__ == "__main__":
    unittest.main()
