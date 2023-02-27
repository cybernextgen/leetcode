import unittest
from typing import List


data = (
    ([3, 2, 2, 3], 3, 2, [2, 2]),
    ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5, [0, 1, 4, 0, 3]),
)


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        next_index = 0
        for current_element in nums:
            if current_element == val:
                continue
            nums[next_index] = current_element
            next_index += 1
        return next_index


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for (
            input_list,
            deleted_num,
            result_length_expected,
            result_list_expected,
        ) in data:
            result = input_list[:]
            result_length = s.removeElement(result, deleted_num)
            self.assertListEqual(result[:result_length], result_list_expected)
            self.assertEqual(result_length, result_length_expected)


if __name__ == "__main__":
    unittest.main()
