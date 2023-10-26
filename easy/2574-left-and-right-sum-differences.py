import unittest
from typing import List
import operator

data = (([10, 4, 8, 3], [15, 1, 11, 22]), ([1], [0]))


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)

        right_sum = [0] * len_nums
        for index in range(len_nums - 1, 0, -1):
            right_sum[index - 1] = nums[index] + right_sum[index]

        left_sum = 0
        for index in range(0, len_nums - 1):
            current_num = nums[index]
            right_sum[index + 1] = abs(current_num + left_sum - right_sum[index + 1])
            left_sum += current_num

        return right_sum


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertListEqual(expected, s.leftRightDifference(input_data))


if __name__ == "__main__":
    unittest.main()
