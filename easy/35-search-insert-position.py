import unittest
from typing import List

data = (
    ([1, 3, 5, 6], 5, 2),
    ([1, 3, 5, 6], 2, 1),
    ([1, 3, 5, 6], 7, 4),
    ([1, 3, 5, 6], 0, 0),
    ([1], 1, 0),
    ([1, 3], 0, 0),
)


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left_index = 0
        right_index = len(nums)
        while left_index < right_index:
            median_index = left_index + (right_index - left_index) // 2
            median_element = nums[median_index]
            if median_element >= target:
                right_index = median_index
                continue
            left_index = median_index + 1
        return left_index


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, target, result in data:
            self.assertEqual(result, s.searchInsert(input_data, target))


if __name__ == "__main__":
    unittest.main()
