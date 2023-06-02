import unittest
from typing import List

data = (
    # ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]),
    # ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121]),
    # ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]),
    ([-5, -3, -2, -1], [1, 4, 9, 25]),
)


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        zero_index = 0
        first_element = nums[0]
        # search for absolute minimum element
        if first_element < 0:
            prev_num = first_element
            for index, n in enumerate(nums):
                if n == 0:
                    zero_index = index
                    break
                if n > 0:
                    if abs(prev_num) > n:
                        zero_index = index
                    else:
                        zero_index = index - 1
                    break
                prev_num = n
                zero_index = index
        right_index = zero_index
        left_index = zero_index - 1
        # calculate squares
        result = []
        while left_index >= 0 or right_index < len(nums):
            if right_index < len(nums) and left_index >= 0:
                right_element = nums[right_index]
                left_element = nums[left_index]
                if right_element > abs(left_element):
                    min_element = left_element
                    left_index -= 1
                else:
                    min_element = right_element
                    right_index += 1
            elif right_index < len(nums):
                min_element = nums[right_index]
                right_index += 1
            else:
                min_element = nums[left_index]
                left_index -= 1
            result.append(min_element**2)
        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertListEqual(s.sortedSquares(input_data), expected)


if __name__ == "__main__":
    unittest.main()
