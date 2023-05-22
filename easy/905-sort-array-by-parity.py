import unittest
from typing import List

data = (
    ([3, 1, 2, 4], [4, 2, 1, 3]),
    ([0], [0]),
    ([0, 2], [0, 2]),
    ([0, 2, 1], [0, 2, 1]),
)


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        if not nums or len_nums == 1:
            return nums

        left_index = 0
        right_index = len_nums - 1

        while left_index < right_index:
            if nums[left_index] % 2:
                if not nums[right_index] % 2:
                    nums[left_index], nums[right_index] = (
                        nums[right_index],
                        nums[left_index],
                    )
                    left_index += 1
                right_index -= 1
            else:
                left_index += 1
        return nums


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertListEqual(s.sortArrayByParity(input_data), expected)


if __name__ == "__main__":
    unittest.main()
