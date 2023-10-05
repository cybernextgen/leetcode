import unittest
from typing import List

data = (([3, 4, 5, 1, 2], 2), ([1, 3, 5], 0), ([2, 1, 4], -1))


class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        len_nums = len(nums)
        if len_nums == 1:
            return 0

        shifts = -1
        for index in range(len_nums - 1, -1, -1):
            current_element = nums[index]
            prev_element = nums[index - 1]
            if prev_element > current_element:
                if shifts == -1:
                    shifts = len_nums - index
                else:
                    return -1
        if shifts == len_nums:
            return 0

        return shifts


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(expected, s.minimumRightShifts(input_data))


if __name__ == "__main__":
    unittest.main()
