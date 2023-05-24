import unittest
from typing import List

data = (
    ([3, 4], [4, 3]),
    ([4, 2, 5, 7], [4, 5, 2, 7]),
    ([2, 3], [2, 3]),
)


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        if not nums or len(nums) == 1:
            return nums
        left_index, right_index = 0, 1
        while left_index < len(nums) - 1:
            left_element_even = nums[left_index] % 2
            right_element_even = nums[right_index] % 2
            index_is_even = left_index % 2
            if index_is_even == left_element_even:
                left_index += 1
                right_index = left_index
            elif index_is_even == right_element_even:
                nums[left_index], nums[right_index] = (
                    nums[right_index],
                    nums[left_index],
                )
                left_index += 1
                right_index = left_index
            right_index += 1
        return nums


class Solution2:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        if not nums or len_nums == 1:
            return nums
        odd_index, even_index = 0, 1
        while odd_index < len_nums and even_index < len_nums:
            odd_element, even_element = nums[odd_index], nums[even_index]
            if not odd_element % 2:
                odd_index += 2
            elif even_element % 2:
                even_index += 2
            else:
                nums[odd_index], nums[even_index] = even_element, odd_element
                odd_index += 2
                even_index += 2
        return nums


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution2()

        for input_data, expected in data:
            self.assertListEqual(s.sortArrayByParityII(input_data), expected)


if __name__ == "__main__":
    unittest.main()
