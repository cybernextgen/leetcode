import unittest
from itertools import combinations
from typing import List, Tuple

data = (([1, 8, 6, 2, 5, 4, 8, 3, 7], 49), ([1, 1], 1))


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_volume = 0
        left_index = 0
        right_index = len(height) - 1

        left_element = height[left_index]
        right_element = height[right_index]
        while left_index != right_index:
            distance = right_index - left_index
            if right_element <= left_element:
                min_height = right_element
                right_index -= 1
                right_element = height[right_index]
            else:
                min_height = left_element
                left_index += 1
                left_element = height[left_index]
            volume = min_height * distance
            if volume > max_volume:
                max_volume = volume
        return max_volume


class Test(unittest.TestCase):
    def test_parse(self):
        s = Solution()

        for input_data, result in data:
            self.assertEqual(s.maxArea(input_data), result)


if __name__ == "__main__":
    unittest.main()
