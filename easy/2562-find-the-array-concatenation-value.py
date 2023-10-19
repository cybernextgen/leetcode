import unittest
from typing import List

data = (([7, 52, 2, 4], 596), ([5, 14, 13, 8, 12], 673))


class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        result = 0
        if not nums:
            return result

        left_index = 0
        right_index = len(nums) - 1
        while left_index < right_index:
            left_val = nums[left_index]
            right_val = nums[right_index]
            result += int(f"{left_val}{right_val}")
            left_index += 1
            right_index -= 1

        if left_index == right_index:
            result += nums[left_index]
        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(s.findTheArrayConcVal(input_data), expected)


if __name__ == "__main__":
    unittest.main()
