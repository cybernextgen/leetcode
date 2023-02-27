import unittest
from typing import List

data = (([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4]),)


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev_element = nums[0]
        next_index = 1
        for i in range(1, len(nums)):
            current_element = nums[i]
            if current_element == prev_element:
                continue
            nums[next_index] = current_element
            prev_element = current_element
            next_index += 1
        return next_index


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, result_length_expected, result_list_expected in data:
            result = input_data[:]
            result_length = s.removeDuplicates(result)
            self.assertListEqual(result[:result_length], result_list_expected)
            self.assertEqual(result_length, result_length_expected)


if __name__ == "__main__":
    unittest.main()
