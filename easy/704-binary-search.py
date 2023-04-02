import unittest
from typing import List

data = (
    # ([-1, 0, 3, 5, 9, 12], 9, 4),
    ([-1, 0, 3, 5, 9, 12], 2, -1),
)


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums_list_len = len(nums)
        if not nums_list_len:
            return -1

        left_index = 0
        right_index = nums_list_len
        while left_index != right_index:
            middle_index = left_index + (right_index - left_index) // 2
            middle_element = nums[middle_index]
            if middle_element > target:
                right_index = middle_index
                continue
            if middle_element < target:
                left_index = middle_index + 1
                continue
            return middle_index
        return -1


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_list, target, index in data:
            self.assertEqual(index, s.search(input_list, target), input_list)


if __name__ == "__main__":
    unittest.main()
