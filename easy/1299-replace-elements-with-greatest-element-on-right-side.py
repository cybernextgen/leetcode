import unittest
from typing import List

data = (([17, 18, 5, 4, 6, 1], [18, 6, 6, 6, 1, -1]), ([400], [-1]))


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if not len(arr):
            return []
        max_element = arr[-1]
        for index in range(len(arr) - 1, -1, -1):
            current_element = arr[index]
            arr[index] = max_element
            if current_element > max_element:
                max_element = current_element
        arr[-1] = -1
        return arr


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(s.replaceElements(input_data), expected)


if __name__ == "__main__":
    unittest.main()
